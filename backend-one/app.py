import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from authentication import sign_up, sign_in

load_dotenv()

app = Flask(__name__)
CORS(app)  # allow frontend to connect

# ---------------- REGISTER API ---------------- #

@app.route("/api/register", methods=["POST"])
def api_register():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    user, error = sign_up(email, password)

    if error:
        return jsonify({"error": error}), 400

    return jsonify({"message": "Registration successful"}), 200


# ---------------- LOGIN API ---------------- #

@app.route("/api/login", methods=["POST"])
def api_login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    user, error = sign_in(email, password)

    if error:
        return jsonify({"error": error}), 401

    return jsonify({
        "message": "Login successful",
        "email": email
    }), 200


if __name__ == "__main__":
    app.run(port=1111, debug=True)
