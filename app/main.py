import xlwings as xw
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

# CORS is required with Office Scripts and Excel on the web
CORS(app)


@app.route("/hello", methods=["POST"])
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
    return book.json()


if __name__ == "__main__":
    app.run(port=5000, debug=True)
