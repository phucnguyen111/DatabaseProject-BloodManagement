from flask import request, jsonify

from main import app

@app.route('/register')
def register_blood_donation():
    name = request.args.get('name')
    
