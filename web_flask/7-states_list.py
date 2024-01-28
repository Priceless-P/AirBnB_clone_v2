#!/usr/bin/python3
"""
Script that starts a Flask web application:
- Routes:
  /states_list: display a HTML page with listen of states sorted by state name
"""
from flask import render_template
from flask import Flask
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def states():
    """Displays all sates"""
    from models import State
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tear_down(exception):
    """Removes current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
