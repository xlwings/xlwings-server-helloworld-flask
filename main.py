import os
import secrets
from functools import wraps

import xlwings as xw
from flask import Flask, abort, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# CORS is only required with Office Scripts
CORS(app)


def auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get("Authorization")
        if not secrets.compare_digest(api_key, os.environ["APP_API_KEY"]):
            abort(401)
        return f(*args, **kwargs)

    return decorated_function


@app.route("/hello", methods=["POST"])
@auth_required
def hello():
    # Instantiate a Book object with the deserialized request body
    book = xw.Book(json=request.json)

    # Use xlwings as usual
    sheet = book.sheets[0]
    cell = sheet["A1"]
    if cell.value == "Hello xlwings!":
        cell.value = "Bye xlwings!"
    else:
        cell.value = "Hello xlwings!"

    # Pass the following back as the response
    return jsonify(book.json())


if __name__ == "__main__":
    app.run(port=8000, debug=True)
