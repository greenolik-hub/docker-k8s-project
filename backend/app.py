from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello from backend!"})

@app.route("/data")
def data():
    return jsonify({
        "service": "backend",
        "status": "running"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)