from flask_app import app
from flask_app import jsonify, os

@app.route("/api")
def Home():
    print(os.getenv("API_LINK_KEY"))
    greet = {
        "home": "Welcome home : )"
    }
    return jsonify(greet)