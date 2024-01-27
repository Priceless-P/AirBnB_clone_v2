#!/usr/bin/python3
"""
Script that starts a Flask web application:
- Routes:
  /cities_by_states: display a HTML page with
lists of states along with cities sorted by state name
"""

from flask import render_template
from flask import url_for
from flask import Flask
import models


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb_filters")
def states():
    """Displays all states"""
    from models import State
    from models import City
    from models import Amenity
    states = models.storage.all(State).values()
    amenities = models.storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def tear_down(exception):
    """Removes current SQLAlchemy Session"""
    models.storage.close()


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port='5000')
