from flask import render_template
from main import app

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/request')
def request():
    return render_template('request.html')