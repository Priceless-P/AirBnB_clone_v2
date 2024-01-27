#!/usr/bin/python3
"""
Script that starts a Flask web application:
- Routes:
  /states_list: display a HTML page with listen of states sorted by state name
"""
from flask import render_template
from markupsafe import escape
from flask import Flask
import models


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states")
def states():
    """Displays all states"""
    from models import State
    states = models.storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route("/states/<id>")
def state_id(id):
    """Display state given its id """
    from models import State
    for state in models.storage.all(State).values():
        if state.id == escape(id):
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def tear_down(exception):
    """Removes current SQLAlchemy Session"""
    models.storage.close()


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port='5000')
