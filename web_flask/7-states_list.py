#!/usr/bin/python3
""" Using Flask and rendering all States"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_States():
    """ Requests list of all states objects """
    all_states = {}
    for state in storage.all(State).values():
        all_states[state.id] = state.name
    # pass dict of state id and state name
    return render_template('7-states_list.html', all_states=all_states)


@app.teardown_appcontext
def refresh_session(exception):
    """ for every request it will close the session and refesh """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
