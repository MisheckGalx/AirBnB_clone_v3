#!/usr/bin/python3
"""app module"""

from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.errorhandler(404)
def page_not_found(error):
    """Handles 404 errors"""
    error_content = {"error": "Not found"}
    return jsonify(error_content), 404


@app.teardown_appcontext
def teardown(exception):
    """Handles the teardown method"""
    storage.close()


if __name__ == '__main__':
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True, debug=True)