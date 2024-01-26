from flask import render_template
from flask import Flask
import models


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def states():
    """Displays all sates"""
    from models import State
    states = models.storage.all(State)

    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tear_down():
    """Removes current SQLAlchemy Session"""
    models.storage.close()


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port='5000')
