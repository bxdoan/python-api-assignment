# Author: Doan Bui (bxdoan93@gmail.com)
# htttps://github.com/bxdoan/python-api-assignment
from app import app
from flask import jsonify

@app.route('/')
def index():
    return jsonify({'message': 'Hello Gigacover!'})
