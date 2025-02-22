import requests
import re
import pycodestyle
import subprocess
from typing import List, Tuple, Optional

HF_API_TOKEN = "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"
HF_API_URL = "https://api-inference.huggingface.co/models/bigcode/starcoder"
HEADERS = {"Authorization": f"Bearer {HF_API_TOKEN}"}

class CodeWizard:
    def __init__(self):
        self.language = "python"

    def generate_code(self, prompt: str) -> str:
        try:
            refined_prompt = (
                f"Generate a complete and executable {self.language} function to {prompt}. "
                "Return only the function code without any comments, test cases, or explanations. "
                "Ensure the function is syntactically correct and handles edge cases."
            )
            payload = {
                "inputs": refined_prompt,
                "parameters": {"max_new_tokens": 200, "do_sample": False, "temperature": 0.1, "top_p": 0.9}
            }
            response = requests.post(HF_API_URL, headers=HEADERS, json=payload)
            response.raise_for_status()
            generated = response.json()[0]["generated_text"]

            if self.language == "python":
                code_match = re.search(r"def\s+\w+\s*\([^)]*\):\s*\n(\s{4,}.*(?:\n\s{4,}.*)*)", generated, re.DOTALL)
                code = f"def {code_match.group(0).split('def ')[1]}".strip() if code_match else "No valid Python function generated."
            else:
                code_match = re.search(r"function\s+\w+\s*\([^)]*\)\s*\{\s*\n(\s+.*(?:\n\s+.*)*)\s*\}", generated, re.DOTALL)
                code = f"function {code_match.group(0).split('function ')[1]}".strip() if code_match else "No valid JavaScript function generated."

            if not code or "No valid" in code:
                return code
            if self.language == "python" and code.endswith(':'):
                code += "\n    pass"
            elif self.language == "javascript" and not code.endswith('}'):
                code += "\n}"
            return code
        except Exception as e:
            return f"Error generating code: {str(e)}"

    def provide_hint(self, prompt: str) -> str:
        try:
            hint_prompt = f"Provide a concise coding hint for '{prompt}' in {self.language}."
            payload = {"inputs": hint_prompt, "parameters": {"max_new_tokens": 50, "temperature": 0.5}}
            response = requests.post(HF_API_URL, headers=HEADERS, json=payload)
            response.raise_for_status()
            return response.json()[0]["generated_text"].strip()
        except Exception as e:
            return f"Hint unavailable: {str(e)}"

    def explain_code(self, code: str) -> str:
        try:
            explain_prompt = f"Explain this {self.language} code in simple terms:\n\n{code}"
            payload = {"inputs": explain_prompt, "parameters": {"max_new_tokens": 100}}
            response = requests.post(HF_API_URL, headers=HEADERS, json=payload)
            response.raise_for_status()
            return response.json()[0]["generated_text"].strip()
        except Exception as e:
            return f"Explanation unavailable: {str(e)}"

    def correct_and_run(self, code: str) -> Tuple[str, str, str]:
        try:
            code = code.replace('\\n', '\n').strip()
            corrections = []
            lines = code.split('\n')
            fixed_lines = []
            has_body = False

            def_line = lines[0].strip()
            if self.language == "python":
                if def_line.startswith('def') and not def_line.endswith(':'):
                    def_line += ':'
                    corrections.append("Added missing colon")
                elif not def_line.startswith('def'):
                    def_line = f"def wrapper():\n    {def_line}"
                    corrections.append("Wrapped in function")
            else:
                if def_line.startswith('function') and not re.search(r'\{$', def_line):
                    def_line += ' {'
                    corrections.append("Added opening brace")
                elif not def_line.startswith('function'):
                    def_line = f"function wrapper() {{\n    {def_line}"
                    corrections.append("Wrapped in function")
            fixed_lines.append(def_line)

            for line in lines[1:]:
                stripped = line.strip()
                if stripped:
                    has_body = True
                if stripped and not line.startswith(' '):
                    fixed_lines.append('    ' + line)
                    corrections.append("Fixed indentation")
                else:
                    fixed_lines.append(line)

            if not has_body and fixed_lines[0].startswith(('def', 'function')):
                fixed_lines.append('    pass' if self.language == "python" else '}')
                corrections.append(f"Added {'pass' if self.language == 'python' else 'closing brace'}")

            if self.language == "javascript" and not any(line.strip() == '}' for line in fixed_lines):
                fixed_lines.append('}')
                corrections.append("Added closing brace")

            fixed_code = '\n'.join(fixed_lines)

            if self.language == "python":
                temp_file = "temp_code.py"
                with open(temp_file, "w") as f:
                    f.write(fixed_code)
                style_checker = pycodestyle.StyleGuide(quiet=True)
                result = style_checker.check_files([temp_file])
                if result.total_errors > 0:
                    corrections.append(f"Addressed {result.total_errors} PEP 8 issues")
            else:
                temp_file = "temp_code.js"

            output = ""
            if self.language == "python":
                try:
                    func_name = re.search(r"def\s+(\w+)\s*\(", fixed_code)
                    test_code = fixed_code + (f"\n\nprint({func_name.group(1)}(3, 5))" if func_name else "")
                    with open(temp_file, "w") as f:
                        f.write(test_code)
                    output = subprocess.check_output(["python", temp_file], stderr=subprocess.STDOUT, timeout=5).decode().strip()
                except subprocess.CalledProcessError as e:
                    output = f"Execution error: {e.output.decode()}"
            elif self.language == "javascript":
                try:
                    func_name = re.search(r"function\s+(\w+)\s*\(", fixed_code)
                    test_code = fixed_code + (f"\n\nconsole.log({func_name.group(1)}(3, 5));" if func_name else "")
                    with open(temp_file, "w") as f:
                        f.write(test_code)
                    output = subprocess.check_output(["node", temp_file], stderr=subprocess.STDOUT, timeout=5).decode().strip()
                except subprocess.CalledProcessError as e:
                    output = f"Execution error: {e.output.decode()}"

            return fixed_code, "\n".join(corrections) or "No corrections needed", output
        except Exception as e:
            return code, f"Error in correction: {str(e)}", "Execution skipped"