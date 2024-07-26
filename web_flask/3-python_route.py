#!/usr/bin/python3
""" This module starts the flask application allowing parameters"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def welcome():
    """The route response to root"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """The route response to hbnb"""
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def c(text):
    """The route response to c route"""
    res = text.replace("_", " ")
    return f"C {res}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<string:text>", strict_slashes=False)
def python(text="is cool"):
    """The route response to python route"""
    res = text.replace("_", " ")
    return f"Python {res}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
