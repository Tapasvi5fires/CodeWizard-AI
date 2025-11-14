An AI-powered Coding Assistant that generates, explains, corrects, and executes code using StarCoder.

🚀 CodeWizard AI
Your Personal AI-Powered Coding Assistant

Created by Tapasvi Panchagnula

🧠 Overview

CodeWizard AI is an intelligent coding assistant built using Flask, HuggingFace StarCoder, and Python execution engine.
It helps developers with:

✔ Code generation
✔ Code explanation
✔ Code correction + execution
✔ Syntax linting
✔ Hints for logic
✔ Multi-language support (Python & JavaScript)

This project includes both:

A Web App (Flask)

A CLI Tool (terminal-based)

🎯 Key Features
✅ 1. AI Code Generation

Uses HuggingFace StarCoder to generate high-quality code based on natural-language prompts.

✅ 2. AI Code Explanation

Explain any code in simple, easy-to-understand language.

✅ 3. Automatic Code Correction

Detects errors using:

Regular expressions

pycodestyle (PEP8 linter)

Custom rule-based fixes

Then rewrites corrected code.

✅ 4. Code Execution Sandbox

Executes user code safely using a temporary file & subprocess.

Supports:

Python

JavaScript

✅ 5. Error Feedback

If execution fails, the assistant returns:

Corrected code

Explanation of corrections

Output / errors from execution

✅ 6. Language Switching

Users can switch between:

"python"

"javascript"

📂 Project Structure
CodeWizard-AI/
│
├── app.py                 # Flask web server
├── main.py                # CLI tool (terminal version)
├── code_wizard.py         # Core AI engine - code generation, correction, execution
├── requirements.txt       # Dependencies
├── templates/
│   └── index.html         # Web UI
├── static/                # CSS/JS assets (currently minimal)
├── security/              # Placeholder directory
├── solutionstotest.txt    # Sample test prompts
└── README.md              # Documentation

🧠 How the System Works (Architecture)
User Input
   │
   ▼
Flask App (app.py)
   │
   ├── generate  →  StarCoder API → AI-generated code
   ├── hint      →  AI suggestion
   ├── correct   →  fix code → run code → return output
   ├── explain   →  explain code using StarCoder
   └── lang      →  change language mode
   │
   ▼
CodeWizard Class (code_wizard.py)
   │
   ├── HuggingFace StarCoder API
   ├── Regex correction system
   ├── PEP8 linting (pycodestyle)
   ├── Subprocess execution engine
   └── Output formatter
   │
   ▼
Web UI (index.html)

🧩 Detailed Explanation — Each Component
📌 code_wizard.py — Core Intelligence Engine

This is the most important file.

Functions inside:
🔹 generate_code(prompt)

Sends your prompt to HuggingFace StarCoder via REST API.
Returns generated code.

🔹 provide_hint(prompt)

Returns a short suggestion/hint using StarCoder.

🔹 explain_code(code)

Explains the logic behind given code.

🔹 correct_and_run(code)

Fixes code step-by-step:

Detect syntax errors

Run pycodestyle to check for issues

Apply corrections (indentation, missing colons, spacing)

Save code to a temp file

Execute using subprocess

Returns:

Fixed code

Explanation of corrections

Execution result

🔹 Language Execution Logic

If language == "python" → run via Python
If language == "javascript" → run via Node.js

📌 app.py — Flask Web Application

Handles all web routes:

Route	Method	Description
/	GET/POST	Main UI
action = generate	POST	Generate code
action = correct	POST	Correct + execute code
action = hint	POST	Provide hint
action = explain	POST	Explain code
action = lang	POST	Switch language

Uses Jinja2 to pass results into index.html.

📌 main.py — CLI Version

A terminal version of CodeWizard.

Features include:

Text-based interface

Code generation

Explanation

Error correction

Code execution

Color coded output using termcolor

Useful for Linux/terminal lovers.

📌 templates/index.html — Web Interface

Simple clean UI:

Input text area

Buttons:

Generate Code

Explain

Get Hint

Correct Code

Change Language

Outputs AI results below form.

🛠️ Installation
1️⃣ Clone the Repository
git clone https://github.com/Tapasvi5fires/CodeWizard-AI.git
cd CodeWizard-AI

2️⃣ Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

3️⃣ Install Requirements
pip install -r requirements.txt

▶️ Running the Web App (Flask)
python app.py


Open in browser:

http://127.0.0.1:5000/

💻 Running the CLI Version
python main.py


You will see a terminal UI similar to:

Welcome to CodeWizard AI
1. Generate Code
2. Correct & Run Code
3. Explain Code
4. Change Language
...

🔧 Environment Variables

You must add your HuggingFace API token inside code_wizard.py or via environment variable:

HF_API_TOKEN = "<your token>"

🧪 Example Usage
Generate Code

Prompt:

write a python function to check prime number


Output:

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

🛡️ Security Notes

Executes code in a limited sandbox, but still be careful with untrusted user input.

Uses temp files and timeout limits to prevent abuse.

🐳 Docker Support (Optional)

If you want, I can create a Dockerfile for you as well.
Just tell me: "Generate Dockerfile for CodeWizard AI"

🤝 Contributing

Pull requests are welcome!

📜 License

MIT License (You can change this if needed.)

🎥 Demo Video

Aicodewizard.mp4 is included in repository.
You can upload it to GitHub Releases or embed it as a GIF.

⭐ Author

Tapasvi Panchagnula
AI Developer • Backend Engineer • ML Enthusiast
