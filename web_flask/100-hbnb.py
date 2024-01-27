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


@app.route("/hbnb")
def states():
    """Displays all states"""
    from models import State
    from models import Amenity
    from models import Place
    states = models.storage.all(State).values()
    amenities = models.storage.all(Amenity).values()
    places = models.storage.all(Place).values()
    Place.amenities

    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places)


@app.teardown_appcontext
def tear_down(exception):
    """Removes current SQLAlchemy Session"""
    models.storage.close()


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port='5000')
