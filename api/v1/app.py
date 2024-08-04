#!/usr/bin/python3
from flask import Flask
from models import storage
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*", {"origins": "0.0.0.0"}})
app.register_blueprint(app_views, url_prefix="/api/v1")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
