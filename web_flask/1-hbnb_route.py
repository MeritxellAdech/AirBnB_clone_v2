#!/usr/bin/python3
""" This module starts the flask application """

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
