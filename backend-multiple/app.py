import os
from flask import Flask, session, render_template, request, redirect, url_for, jsonify
from dotenv import load_dotenv
from authentication import sign_up, sign_in, verify_google_token

load_dotenv()

app = Flask(__name__, template_folder=".")


# Pass Firebase config to frontend dynamically
@app.context_processor
def inject_firebase_config():
    return dict(firebase_config={
        "apiKey": os.getenv("FIREBASE_API_KEY"),
        "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
        "projectId": os.getenv("FIREBASE_PROJECT_ID"),
        "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
        "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
        "appId": os.getenv("FIREBASE_APP_ID"),
        "measurementId": os.getenv("FIREBASE_MEASUREMENT_ID"),
    })


@app.route("/")
def index():
    return render_template("index.html")


# ---------------- LOGIN ---------------- #

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        if not email or not password:
            return render_template("login.html", error="Please enter email and password.")

        user, error = sign_in(email, password)

        if error:
            return render_template("login.html", error="Login failed.")

        session["user_email"] = email
        return redirect(url_for("dashboard"))

    return render_template("login.html")


# ---------------- REGISTER ---------------- #

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        if not email or not password:
            return render_template("register.html", error="Please enter email and password.")

        user, error = sign_up(email, password)

        if error:
            return render_template("register.html", error="Signup failed.")

        session["user_email"] = email
        return redirect(url_for("dashboard"))

    return render_template("register.html")


# ---------------- GOOGLE SESSION ---------------- #

@app.route("/google-session", methods=["POST"])
def google_session():
    data = request.get_json()
    id_token = data.get("idToken")

    if not id_token:
        return jsonify({"error": "No token provided"}), 400

    user, error = verify_google_token(id_token)

    if error:
        return jsonify({"error": "Invalid Google token"}), 401

    session["user_email"] = user.get("email")

    return jsonify({"message": "Google login successful"}), 200


# ---------------- DASHBOARD ---------------- #

@app.route("/dashboard")
def dashboard():
    if "user_email" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html", email=session.get("user_email"))


@app.route("/logout")
def logout():
    session.pop("user_email", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(port=1111, debug=True)
