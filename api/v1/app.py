#!/usr/bin/python3
"""Flask App"""

import os
from flask_cors import CORS
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.debug = True

app.register_blueprint(app_views)

cors = CORS(app, origins="0.0.0.0")


@app.teardown_appcontext
def close_storage(exception):
    """closes the storage"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """a handler for 404 errors"""
    return {"error": "Not found"}, 404


if __name__ == "__main__":
    """main method"""
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = os.getenv("HBNB_API_PORT", "5000")
    app.run(host=host, port=port, threaded=True)
~                                                
