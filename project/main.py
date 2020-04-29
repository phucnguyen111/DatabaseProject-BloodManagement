from flask import Flask, render_template


app = Flask(__name__, static_folder='templates')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/request')
def request():
    return render_template('request.html')
if __name__ == '__main__':
    app.run(debug=True)