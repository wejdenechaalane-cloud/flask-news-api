
from flask import Flask, jsonify
from flask_cors import CORS
import json
from pathlib import Path
import datetime

app = Flask(__name__)

# Allow Flutter Web to access this Flask API
CORS(app)

# Find news_data.json in the same folder
NEWS_FILE = Path(__file__).with_name("news_data.json")


@app.route("/")
def index():
    return "Welcome ENSIA Students from Flask!"


@app.route("/news.all.get")
def get_news_all_articles():
    with NEWS_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    app.logger.debug("News articles loaded: %s", len(data))
    return jsonify(data)


@app.route("/news.categories.get")
def get_news_categories():
    time_now_str = datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    data = {
        "title": "List of Categories",
        "time": time_now_str,
        "categories": [
            {"id": 1, "name": "Sports"},
            {"id": 2, "name": "Politics"},
            {"id": 3, "name": "Education"}
        ]
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
