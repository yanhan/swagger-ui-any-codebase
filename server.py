import os.path
from datetime import datetime
from functools import wraps, update_wrapper

from flask import Flask, jsonify, make_response, send_from_directory

# We use this to prevent caching of `/api-docs.yml`
# Credits: https://arusahni.net/blog/2014/03/flask-nocache.html
def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers["Last-Modified"] = datetime.now()
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, pre-check=0, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "-1"
        return response
    return update_wrapper(no_cache, view)

app = Flask(__name__)

SWAGGER_UI_DIST_DIR = "swagger-ui-dist"

@app.route("/swagger-ui/")
def swagger_ui():
    return send_from_directory(SWAGGER_UI_DIST_DIR, "index.html")

@app.route("/swagger-ui/<asset>")
def swagger_assets(asset):
    return send_from_directory(SWAGGER_UI_DIST_DIR, asset)

@app.route("/api-docs.yml")
@nocache
def swagger_api_docs_yml():
    return send_from_directory(".", "api-docs.yml")

if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True,)
