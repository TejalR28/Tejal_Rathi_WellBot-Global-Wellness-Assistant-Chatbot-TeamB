## Firebase setup (high-level steps)

These are the typical steps you’ll follow to hook this backend up to Firebase:

1. **Create a Firebase project**
   - Go to the Firebase console and create a new project (or use an existing one).

2. **Enable Email/Password auth**
   - In the Firebase console, go to **Authentication → Sign-in method**.
   - Enable **Email/Password**.

3. **Create a Web App (for frontend use, if any)**
   - In the Firebase console, go to **Project Overview → Add app → Web**.
   - Register the app and copy the config snippet (the `apiKey`, `authDomain`, etc.) for your frontend.

4. **Backend credentials / config**
   - Decide how you want to talk to Firebase from the backend:
     - If you are using **Firebase Admin SDK**, download a **service account JSON** from **Project settings → Service accounts**.
     - Store this JSON file **outside of git** (it should be git-ignored) and reference it via an environment variable.
   - Keep all secrets (API keys, service account paths, etc.) in a `.env` file that is **not committed**.

5. **Create a `.env` file**
   - In the project root, create a file named `.env` and put your config in it, for example:

   ```bash
   FIREBASE_API_KEY=your_firebase_api_key_here
   FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
   FIREBASE_PROJECT_ID=your-project-id
   FIREBASE_STORAGE_BUCKET=your-project.appspot.com
   FIREBASE_MESSAGING_SENDER_ID=your_sender_id
   FIREBASE_APP_ID=your_app_id
   FIREBASE_SERVICE_ACCOUNT_PATH=./firebase_service_account.json
   ```

---

## Install dependencies

````bash
pip install -r requirements.txt

---


1. **Make sure `.env` exists**
   - Ensure you have created a `.env` file in the project root with the required Firebase-related variables.

2. **Run the Flask app**

   ```bash
   python app.py

   ````
   then run html file

---
