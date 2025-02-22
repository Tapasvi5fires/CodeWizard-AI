import requests
import re
import pycodestyle
import subprocess
from termcolor import colored
from typing import List, Tuple, Optional
import sys

# --- Configuration ---
HF_API_TOKEN = "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"  # Your Hugging Face API token
HF_API_URL = "https://api-inference.huggingface.co/models/bigcode/starcoder"
HEADERS = {"Authorization": f"Bearer {HF_API_TOKEN}"}

# --- Core Assistant ---
class CodeWizard:
    def __init__(self):
        self.language = "python"

    def generate_code(self, prompt: str) -> str:
        """Generate only the function code using strict extraction."""
        try:
            refined_prompt = (
                f"Generate a complete and executable {self.language} function to {prompt}. "
                "Return only the function code without any comments, test cases, or explanations. "
                "Ensure the function is syntactically correct and handles edge cases."
            )
            payload = {
                "inputs": refined_prompt,
                "parameters": {
                    "max_new_tokens": 200,
                    "do_sample": False,
                    "temperature": 0.1,
                    "top_p": 0.9
                }
            }
            print(f"DEBUG: Sending payload: {payload}")
            response = requests.post(HF_API_URL, headers=HEADERS, json=payload)
            print(f"DEBUG: Status code: {response.status_code}")
            print(f"DEBUG: Raw response: {response.text}")
            response.raise_for_status()
            generated = response.json()[0]["generated_text"]

            # Strict extraction of function only
            if self.language == "python":
                code_match = re.search(r"def\s+\w+\s*\([^)]*\):\s*\n(\s{4,}.*(?:\n\s{4,}.*)*)", generated, re.DOTALL)
                if code_match:
                    code = f"def {code_match.group(0).split('def ')[1]}".strip()
                else:
                    return f"No valid {self.language} function generated."
            else:  # javascript
                code_match = re.search(r"function\s+\w+\s*\([^)]*\)\s*\{\s*\n(\s+.*(?:\n\s+.*)*)\s*\}", generated, re.DOTALL)
                if code_match:
                    code = f"function {code_match.group(0).split('function ')[1]}".strip()
                else:
                    return f"No valid {self.language} function generated."

            if not code:
                return f"No valid {self.language} function generated."
            if self.language == "python" and code.endswith(':'):
                code += "\n    pass"
            elif self.language == "javascript" and not code.endswith('}'):
                code += "\n}"
            return code
        except requests.exceptions.RequestException as e:
            error_msg = f"Error generating code: {str(e)}"
            if hasattr(e, 'response') and e.response is not None:
                error_msg += f"\nAPI Response: {e.response.text}"
            return error_msg
        except Exception as e:
            return f"Unexpected error in code generation: {str(e)}"

    def provide_hint(self, prompt: str) -> str:
        """Provide a more detailed, language-specific hint."""
        prompt_lower = prompt.lower()
        if "sum" in prompt_lower:
            if self.language == "python":
                return "Define a function with two parameters and use 'return a + b' to add them. Handle floats and integers."
            else:  # javascript
                return "Create a function with two parameters; use 'return a + b'. Consider 'Number()' for string inputs."
        elif "loop" in prompt_lower:
            if self.language == "python":
                return "Use 'for i in range(n):' for a counted loop or 'for item in list:' for iteration."
            else:  # javascript
                return "Use 'for (let i = 0; i < n; i++)' for a loop or 'for...of' for arrays."
        else:
            return f"Start with a function definition in {self.language} and break your task into small, logical steps."

    def correct_and_run(self, code: str) -> Tuple[str, str, str]:
        """Correct and execute code with robust handling."""
        try:
            code = code.replace('\\n', '\n').strip()
            print(f"DEBUG: Correcting and running code: {code}")
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
            else:  # javascript
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

            output = "Execution not supported for JavaScript in this demo."
            if self.language == "python":
                try:
                    func_name = re.search(r"def\s+(\w+)\s*\(", fixed_code)
                    test_code = fixed_code
                    if func_name:
                        func_name = func_name.group(1)
                        test_code += f"\n\nprint({func_name}(3, 5))"
                    with open(temp_file, "w") as f:
                        f.write(test_code)
                    output = subprocess.check_output(
                        ["python", temp_file],
                        stderr=subprocess.STDOUT,
                        timeout=5
                    ).decode().strip()
                except subprocess.TimeoutExpired:
                    output = "Error: Execution timed out after 5 seconds."
                except subprocess.CalledProcessError as e:
                    output = f"Execution error: {e.output.decode()}"
                except Exception as e:
                    output = f"Error executing code: {str(e)}"

            return fixed_code, "\n".join(corrections) or "No corrections needed", output
        except Exception as e:
            return code, f"Error in correction: {str(e)}", "Execution skipped"

# --- Hackathon CLI ---
def run_codewizard():
    wizard = CodeWizard()
    print(colored("=== CodeWizard AI: Your Hackathon Hero ===", "cyan"))
    print(colored("Commands: generate, hint, correct, lang [python|javascript], exit", "yellow"))

    while True:
        try:
            cmd = input(colored("\n> ", "green")).strip().lower().split()
            if not cmd:
                continue

            action = cmd[0]
            if action == "exit":
                print(colored("CodeWizard signing off. Good luck winning!", "cyan"))
                break

            elif action == "generate":
                prompt = input(colored("Enter prompt: ", "blue"))
                code = wizard.generate_code(prompt)
                print(colored("Generated Code:", "magenta"))
                print(code)

            elif action == "hint":
                prompt = input(colored("Enter prompt for hint: ", "blue"))
                hint = wizard.provide_hint(prompt)
                print(colored("Hint:", "yellow"))
                print(hint)

            elif action == "correct":
                code = input(colored("Enter code to correct/run: ", "blue"))
                fixed, corrections, output = wizard.correct_and_run(code)
                print(colored("Fixed Code:", "magenta"))
                print(fixed)
                print(colored("Corrections:", "yellow"))
                print(corrections)
                print(colored("Output:", "green"))
                print(output)

            elif action == "lang":
                if len(cmd) < 2 or cmd[1] not in ["python", "javascript"]:
                    print(colored("Usage: lang [python|javascript]", "red"))
                else:
                    wizard.language = cmd[1]
                    print(colored(f"Language set to {wizard.language}", "cyan"))

            else:
                print(colored("Invalid command. Try again!", "red"))

        except KeyboardInterrupt:
            print(colored("\nInterrupted. Exiting...", "red"))
            break
        except Exception as e:
            print(colored(f"Error in CLI: {str(e)}", "red"))

if __name__ == "__main__":
    if "your_huggingface_api_token_here" in HF_API_TOKEN:
        print(colored("Error: Set your Hugging Face API token in HF_API_TOKEN.", "red"))
        sys.exit(1)
    run_codewizard()