from flask import Flask, request, render_template
from code_wizard import CodeWizard

app = Flask(__name__)
wizard = CodeWizard()

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    if request.method == 'POST':
        action = request.form.get('action')
        prompt = request.form.get('prompt', '')
        code = request.form.get('code', '')
        if action == 'generate':
            result = wizard.generate_code(prompt)
        elif action == 'hint':
            result = wizard.provide_hint(prompt)
        elif action == 'correct':
            fixed, corrections, output = wizard.correct_and_run(code)
            result = f"Fixed Code:\n{fixed}\n\nCorrections:\n{corrections}\n\nOutput:\n{output}"
        elif action == 'explain':
            result = wizard.explain_code(code)
        elif action == 'lang':
            wizard.language = prompt.lower()
            result = f"Language set to {wizard.language}"
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)