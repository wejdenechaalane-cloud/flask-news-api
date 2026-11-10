FLASK NEWS API - VERCEL DEPLOYMENT

Files:
- app.py: the Flask backend and its three endpoints
- news_data.json: the ten news articles
- requirements.txt: Python packages

DEPLOY:
1. Upload this folder to a GitHub repository.
2. Sign in to Vercel with GitHub and import that repository.
3. Keep the project root and build settings at their defaults.
4. Click Deploy.
5. Open the deployment URL and test:
   /
   /news.all.get
   /news.categories.get

LOCAL TEST (Windows):
1. Open Command Prompt in this folder.
2. Run: py -m venv .venv
3. Run: .venv\Scripts\activate
4. Run: py -m pip install -r requirements.txt
5. Run: py app.py
6. Visit http://127.0.0.1:8080/

Note: Vercel's native Flask support does not require a separate Gunicorn start command.
