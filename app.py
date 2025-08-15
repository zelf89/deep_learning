from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Flask API on Render!"})

@app.route('/api/test')
def test():
    return jsonify({"status": "working"})