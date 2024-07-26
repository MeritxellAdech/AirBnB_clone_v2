#!/usr/bin/python3
""" This module starts the flask application allowing parameters"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def welcome():
    """The function displays Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """This function displays HBNB"""
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def c_message(text):
    """This function displays the C message passed as URL parameter"""
    res = text.replace("_", " ")
    return f"C {res}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<string:text>", strict_slashes=False)
def python(text="is cool"):
    """The route response to python route"""
    res = text.replace("_", " ")
    return f"Python {res}"


@app.route("/number/<int:num>", strict_slashes=False)
def show_num(num):
    """This function displays the number passed as URL parameter"""
    return f"{num} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
