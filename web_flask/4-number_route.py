#!/usr/bin/python3
"""
Script that starts a Flask web application:
- Routes:
  - /: display “Hello HBNB!”
  /hbnb: display “HBNB”
  /c/<text>: display “C ”, followed by the value of the text
  /python/<text>: display “Python ”, followed by the value of the text
  /number/<n>: display “n is a number” only if n is an integer
"""

from flask import Flask
from markupsafe import escape


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """Displays Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Displays HBNB"""
    return "HBNB!"


@app.route("/c/<text>")
def text(text):
    """Displays C followed by text"""
    return "C {}".format(escape(text.replace('_', ' ')))


@app.route("/python")
@app.route("/python/<text>")
def python(text="is cool"):
    """Displays Python followed by text"""
    return "Python {}".format(escape(text.replace('_', ' ')))


@app.route("/number/<int:n>")
def number(n):
    """Displays n only if it is an integer"""
    return "{} is a number".format(escape(n))


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port='5000')
