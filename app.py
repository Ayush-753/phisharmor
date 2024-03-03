import phishingemail as pe
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/email', methods=["GET", "POST"])
def email():
    if request.method == 'POST':
        email = request.form['email']
        email_analyse = pe.analyse_email([email])
    return render_template('email.html',**locals())

@app.route('/learn', methods=["GET", "POST"])
def learn():
    return render_template('learn.html')

@app.route('/phishing', methods=["GET", "POST"])
def phishing():
    return render_template('phishing.html')

@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    return render_template('quiz.html')

if __name__ == '__main__':
    app.run(debug=True)