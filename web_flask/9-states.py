#!/usr/bin/python3
""" Using Flask and rendering all States"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def display_All_States():
    """ Requests all states """
    all_states = storage.all(State).values()
    return render_template('9-states.html', has_id=0, all_states=all_states)

@app.route('/states/<id>', strict_slashes=False)
def display_States(id):
    """ Requests all states or 1 state with its cities """
    all_states = storage.all(State).values()
    all_states = all_states.get(id, 0)
    return render_template('9-states.html', has_id=1, all_states=all_states)

@app.teardown_appcontext
def refresh_session(exception):
    """ for every request it will close the session and refesh """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
