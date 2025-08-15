from flask import Flask, jsonify, request,render_template

app = Flask(__name__)

@app.route('/')
def home():
    # return jsonify({"message": "Hello from Flask API on Render hahha!"})
    return render_template('index.html')

@app.route('/api/test')
def test():
    return jsonify({"status": "working"})



@app.route('/api/receive', methods=['POST'])
def receive_data():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    return jsonify({
        "status": "success",
        "received": {
            "name": name,
            "age": age
        }
    })