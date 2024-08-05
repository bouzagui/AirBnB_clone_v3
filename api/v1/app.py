#!/usr/bin/python3
"""models doc"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from flask_cors import CORS
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views, url_prefix="/api/v1")


@app.teardown_appcontext
def close(error):
    """close storage"""
    storage.close()

if os.getenv("HBNB_API_HOST"):
    host = os.getenv("HBNB_API_HOST")
else:
    host = "0.0.0.0"

if os.getenv("HBNB_API_PORT"):
    port = os.getenv("HBNB_API_PORT")
else:
    port = 5000


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)