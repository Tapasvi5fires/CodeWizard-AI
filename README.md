# 🚀 CodeWizard AI  
### **Your Personal AI-Powered Coding Assistant**  
*Created by **Tapasvi Panchagnula***  

---

## ![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-black)
![HuggingFace](https://img.shields.io/badge/HuggingFace-StarCoder-yellow)
![JavaScript](https://img.shields.io/badge/JavaScript-Execution-orange)
![PythonRunner](https://img.shields.io/badge/Python-Execution-green)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📌 **Overview**

**CodeWizard AI** is an AI-powered coding assistant that lets you:

✨ Generate code  
✨ Correct code  
✨ Run code  
✨ Explain code  
✨ Get instant AI hints  

…all inside a beautiful **space-themed interface** with glowing animations, cosmic visuals, and smooth UI.

It supports both **Python and JavaScript**, making it ideal for:

- Hackathons  
- Fast prototyping  
- Beginners learning programming  
- Developers who need quick snippets  
- Anyone wanting an AI assistant without complex setup  

---

# 📑 Table of Contents
- [Features](#features)
- [Live Demo UI Preview](#live-demo-ui-preview)
- [Tech Stack](#tech-stack)
- [Project Architecture](#project-architecture)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [For Recruiters](#for-recruiters)

---

# ✨ Features

### 🧠 **AI-Generated Code (StarCoder via HuggingFace API)**
Enter a prompt → instantly get clean, usable Python or JS code.

### 🔧 **Code Correction**
Uses `pycodestyle` + rule-based cleanup to:

- Fix indentation  
- Remove extra whitespace  
- Suggest improvements  

### ▶️ **Run Code (Python + JavaScript)**
Your code is executed safely using:

- Python → `subprocess.run(["python3"])`  
- JavaScript → `subprocess.run(["node"])`  

Output/errors are shown instantly.

### 📘 **Explain Code**
AI generates beginner-friendly explanations of any code snippet.

### 💡 **AI Hints**
Provides language-specific suggestions to improve your code.

### 🌌 **Cosmic UI**
- Animated background  
- Particle effects  
- Neon buttons & glowing inputs  
- Smooth transitions  

---

# 🌠 Tech Stack

### **Backend**
| Technology | Purpose |
|-----------|---------|
| **Flask** | API server |
| **Python** | Logic/validators/execution |
| **subprocess** | Safe code execution |
| **Hugging Face API (StarCoder)** | AI model |

### **Frontend**
| Technology | Purpose |
|-----------|---------|
| **HTML5** | Layout |
| **CSS3 (neon + space theme)** | UI design |
| **JavaScript** | Frontend logic |
| **Canvas animations** | Cosmic effects |

---

# 🧩 Project Architecture

```text
┌────────────────────────────────────────┐
│              Frontend UI               │
│  (HTML • CSS • Canvas • JavaScript)    │
└───────────────────────┬────────────────┘
                        ▼
┌────────────────────────────────────────┐
│             Flask Backend              │
│     /generate /explain /correct /run   │
└───────────────────────┬────────────────┘
                        ▼
        ┌────────────────────────────────┐
        │ HuggingFace StarCoder API      │
        │  (code generation/explanation) │
        └────────────────────────────────┘
                        ▼
        ┌────────────────────────────────┐
        │ Local Code Execution Engine    │
        │ Python → subprocess (python3)  │
        │ JS → subprocess (node)         │
        └────────────────────────────────┘
```
⚙️ How It Works (Based on Real Source Code)
1. Backend Routing (main.py)
The app exposes routes:

/generate_code

/correct_code

/run_code

/explain_code

/hint

/set_language

Each accepts JSON from the frontend.

2. HuggingFace StarCoder Integration
API call:

python
Copy code
payload = {
    "inputs": prompt,
    "parameters": {"max_new_tokens": 200}
}
3. Code Execution
Python:

python
Copy code
subprocess.run(["python3"], input=code, capture_output=True)
JavaScript:

python
Copy code
subprocess.run(["node"], input=code, capture_output=True)
4. Corrections
Uses:

pycodestyle

small rule-based indentation fixes

5. Frontend
Fully interactive interface:

glowing buttons

animated starfield

dropdown to toggle language

sections for generated text/output

🛠 Installation
bash
Copy code
git clone https://github.com/Tapasvi5fires/CodeWizard-AI.git
cd CodeWizard-AI
pip install -r requirements.txt
No GPU or special setup required.

▶️ Usage
Start the Flask Server
bash
Copy code
python3 main.py
Open browser at:

cpp
Copy code
http://127.0.0.1:5000
Inside the App:
Select Python / JavaScript

Type a prompt → Generate code

Paste code → Correct or Explain

Click Run → Executes code and shows output

📁 Folder Structure
text
Copy code
CodeWizard-AI/
│
├── main.py                 # Flask backend
│
├── templates/
│   └── index.html          # Frontend page
│
├── static/
│   ├── style.css           # UI styling (neon/cosmic)
│   ├── script.js           # Client logic + API calls
│   ├── bg.mp4              # Background animation
│   └── favicon.png         # Icon
│
└── requirements.txt
🚀 Future Enhancements
Add syntax tree-based corrections

Add local LLM mode (no API required)

Add support for more languages (Java, C++)

Add unit test generator

Implement session history

Add code quality scoring

🤝 Contributing
PRs are welcome!
Fork → Edit → Pull Request.

📜 License
MIT License — use freely.

🎯 For Recruiters
This project demonstrates skills in:

AI Integration (HuggingFace API, Model Prompting)

Backend Engineering (Flask, REST APIs)

Frontend Engineering (HTML, CSS animations, JS)

Secure code execution (Python/Node subprocess management)

Full-stack development

UI/UX design with animations

I built CodeWizard AI end-to-end, including:

AI logic

Execution engine

Error handling

Cosmic UI

Deployment-ready Flask app

