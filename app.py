from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

USERNAME = "studente"
PASSWORD = "password"

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == USERNAME and password == PASSWORD:
            return redirect(url_for('dashboard'))
        else:
            error = "Credenziali errate"
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    esami = [
        {'nome': 'Fisica medica', 'cfu': 7, 'voto': 27},
        {'nome': 'Chimica', 'cfu': 8, 'voto': 28},
        {'nome': 'Biologia', 'cfu': 10, 'voto': 27},
        {'nome': 'Anatomia', 'cfu': 16, 'voto': 29},
    ]
    return render_template('dashboard.html', esami=esami)