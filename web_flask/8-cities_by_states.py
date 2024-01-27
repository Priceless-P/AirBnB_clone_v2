#!/usr/bin/python3
"""
Script that starts a Flask web application:
- Routes:
  /cities_by_states: display a HTML page with
lists of states along with cities sorted by state name
"""

from flask import render_template
from flask import Flask
import models


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/cities_by_states")
def states():
    """Displays all sates"""
    from models import State
    states = models.storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def tear_down(exception):
    """Removes current SQLAlchemy Session"""
    models.storage.close()


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port='5000')
