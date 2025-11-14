# 🚀 CodeWizard AI  
### **Your Personal AI-Powered Coding Assistant**  
*Created by **Tapasvi Panchagnula***  

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-black)
![HuggingFace](https://img.shields.io/badge/StarCoder-AI%20Model-yellow)
![JavaScript](https://img.shields.io/badge/JavaScript-Execution-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

---

# 📌 Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Architecture Overview](#architecture-overview)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Usage (Web App)](#usage-web-app)
- [Usage (CLI Version)](#usage-cli-version)
- [How It Works](#how-it-works)
- [API & Internal Logic](#api--internal-logic)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

# 🎯 About the Project  
**CodeWizard AI** is an end‑to‑end coding assistant that helps developers generate, explain, correct, and execute code using **HuggingFace StarCoder**, Flask, and Python.  
It works as both:  
- 🌐 A **Web Application**, and  
- 💻 A **CLI Terminal Application**

This project showcases full‑stack AI integration, backend automation, prompt engineering, syntax correction, and safe code execution.

---

# ⭐ Features

### ✔ Code Generation  
Generate new code from natural language using StarCoder.

### ✔ Code Explanation  
Explain any provided code in simple human terms.

### ✔ Code Correction  
Fix syntax & indentation issues using:  
- Regex corrections  
- PEP8 linting (pycodestyle)  
- Rule-based cleanup

### ✔ Code Execution  
Safely execute Python or JavaScript using a sandboxed `subprocess`.

### ✔ Hint Generation  
Get small hints for improvements or debugging.

### ✔ Language Switching  
Switch between **Python** and **JavaScript** modes.

---

# 🔧 Technology Stack

| Component | Technology |
|----------|------------|
| Backend  | Flask |
| AI Model | HuggingFace StarCoder |
| Linting | pycodestyle |
| Code Execution | subprocess + temp files |
| Frontend | HTML (Jinja2 Template) |
| CLI Tool | Python + termcolor |

---

# 🏗 Architecture Overview

```
┌──────────────────────┐
│      User Input      │
└───────────┬──────────┘
            ▼
     ┌───────────────┐
     │   Flask App   │
     └──────┬────────┘
            ▼
┌──────────────────────────────┐
│     CodeWizard Engine        │
│ generate | explain | correct │
│ lint | run | hint | execute  │
└───────────────┬──────────────┘
                ▼
       ┌────────────────┐
       │ HuggingFace AI │
       └────────────────┘
```

---

# 📁 Project Structure

```
CodeWizard-AI/
│
├── app.py                 # Flask Web Server
├── main.py                # CLI Application
├── code_wizard.py         # AI Logic (StarCoder + Execution + Linting)
├── templates/
│   └── index.html         # Frontend Template
├── static/                # CSS/JS (future use)
├── solutionstotest.txt    # Test prompts
├── requirements.txt
└── README.md              # Documentation
```

---

# ⚙ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Tapasvi5fires/CodeWizard-AI.git
cd CodeWizard-AI
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scriptsctivate     # Windows
```

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

---

# ▶ Usage (Web App)

Run:
```bash
python app.py
```

Then open in browser:
```
http://127.0.0.1:5000/
```

---

# 💻 Usage (CLI Version)

```bash
python main.py
```

You will see options for:
- Generate Code  
- Correct & Run  
- Explain Code  
- Get Hints  
- Switch Language  

---

# 🧠 How It Works

### 🔹 Code Generation  
StarCoder receives your prompt → returns generated code.

### 🔹 Code Correction  
`correct_and_run()` performs:  
- Regex-based cleanup  
- PEP8 lint check  
- Auto-fixes  
- Test execution  
- Returns corrected code + explanation

### 🔹 Execution  
Python → run via `python`  
JS → run via `node`

Executed in a **temp sandbox file**.

---

# 🔌 API & Internal Logic Breakdown

### 📌 `generate_code(prompt)`
Uses StarCoder endpoint to generate code.

### 📌 `provide_hint(prompt)`
Returns micro‑suggestions for debugging.

### 📌 `explain_code(code)`
Explains code step-by-step.

### 📌 `correct_and_run(code)`
1. Detects syntax issues  
2. Lints using pycodestyle  
3. Fixes structure  
4. Executes safely  
5. Returns:  
   - corrected code  
   - explanation  
   - runtime output  

---

# 🚀 Future Enhancements

- Add **Dark UI Theme**
- Support **C++**, **Java**, **Go**
- Add **Docker deployment**
- Add **Authentication**
- Real-time collaborative editing
- Syntax highlighting in UI
- GPU-powered StarCoder inference

---

# 🤝 Contributing

1. Fork this repository  
2. Create a new branch  
3. Commit changes  
4. Open a Pull Request  

---

# 📜 License  
MIT License

---

# 👤 Author  
**Tapasvi Panchagnula**  
AI/ML Engineer • Backend Developer • Python Specialist  
