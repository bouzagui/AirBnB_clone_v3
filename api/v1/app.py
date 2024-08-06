#!/usr/bin/python3
"""models doc"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views, url_prefix="/api/v1")


@app.errorhandler(404)
def page_not_found(e):
    """page not found"""
    return jsonify({"error": "Not found"}), 404


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
    app.run(host=host, port=port, threaded=True, debug=True)
