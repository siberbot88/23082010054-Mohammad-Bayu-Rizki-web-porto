from flask import Flask,jsonify, request
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def entry_point():
    
    return jsonify(message='hello world')