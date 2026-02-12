## Prerequisites

- **Python**: 3.8+ installed
- **pip**: Python package manager
- **Firebase project**: created in the Firebase console

## 1. Clone and install dependencies

# Install Python dependencies
pip install -r requirements.txt
```

## 2. Configure Firebase (.env file)

Create a file named `.env` in the project root (same folder as `app.py`) and add your Firebase config:

FIREBASE_API_KEY=your_firebase_api_key
FIREBASE_AUTH_DOMAIN=your_project_id.firebaseapp.com
FIREBASE_PROJECT_ID=your_project_id
FIREBASE_STORAGE_BUCKET=your_project_id.appspot.com
FIREBASE_MESSAGING_SENDER_ID=your_messaging_sender_id
FIREBASE_APP_ID=your_app_id
FIREBASE_MEASUREMENT_ID=your_measurement_id
```

### How to get these values from Firebase

1. Go to the **Firebase console** and open your project.
2. In **Project Overview**, click the **web (`</>`) app** icon (or create a new web app).
3. Firebase shows a config object like:
   ```js
   const firebaseConfig = {
     apiKey: "…",
     authDomain: "…",
     projectId: "…",
     storageBucket: "…",
     messagingSenderId: "…",
     appId: "…",
     measurementId: "…"
   };
   ```
4. Copy each field into the matching variable in your `.env` file.

Also, in the Firebase console:

- **Enable Authentication providers**:
  - Go to **Build → Authentication → Sign-in method**.
  - Enable **Email/Password**.
  - Enable **Google** and complete the setup (add authorized domains, etc.).

## 3. Run the application

From the project root (with your virtual environment activated and `.env` configured):

```bash
python app.py
```

The app will start on `http://127.0.0.1:1111/` (or `http://localhost:1111/`).

Open that URL in your browser to access the login, registration, and dashboard pages.

