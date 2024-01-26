#!/usr/bin/python3
"""
Script that starts a Flask web application:
- Routes:
  - /: display “Hello HBNB!”
"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """Displays Hello HBNB"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port='5000')
