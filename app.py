from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Backend is working!"

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()

    description = data.get("description", "")

    return jsonify({
        "Steps to Reproduce": [
            "Open the application",
            "Navigate to the feature",
            "Perform the action",
            "Observe the issue"
        ],
        "Expected Behavior": "Should work without errors",
        "Actual Behavior": description,
        "Possible Causes": [
            "Unhandled exception",
            "Auth/session issue"
        ],
        "Severity": "High"
    })