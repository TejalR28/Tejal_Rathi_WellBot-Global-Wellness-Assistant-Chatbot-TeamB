import os
import requests
import pyrebase
from dotenv import load_dotenv

load_dotenv()

config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
    "measurementId": os.getenv("FIREBASE_MEASUREMENT_ID"),
    "databaseURL": "",
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


# ---------------- EMAIL AUTH ---------------- #

def sign_up(email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        return user, None
    except Exception as e:
        return None, str(e)


def sign_in(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return user, None
    except Exception as e:
        return None, str(e)


# ---------------- GOOGLE VERIFY ---------------- #

def verify_google_token(id_token):
    try:
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:lookup?key={os.getenv('FIREBASE_API_KEY')}"

        response = requests.post(url, json={"idToken": id_token})
        data = response.json()

        if "users" in data:
            return data["users"][0], None
        return None, "Invalid token"

    except Exception as e:
        return None, str(e)

