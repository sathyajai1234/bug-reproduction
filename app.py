from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Home route
@app.route("/")
def home():
    return "Backend is working!"

# Generate bug report route
@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()

        if not data or "description" not in data:
            return jsonify({
                "error": "Description is required"
            }), 400

        description = data["description"]

        response = {
            "steps": [
                "Open the application",
                f"Perform action: {description}",
                "Observe the issue"
            ],
            "expected": "Application should work correctly without errors",
            "actual": f"Bug occurs when: {description}",
            "possible_causes": [
                "Invalid input handling",
                "Backend validation missing",
                "Unexpected frontend behavior"
            ],
            "severity": "Medium"
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)