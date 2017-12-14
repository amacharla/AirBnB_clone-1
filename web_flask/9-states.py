#!/usr/bin/python3
""" Using Flask and rendering all States"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def display_All_States():
    """ Renders all states """
    all_states = storage.all(State).values()
    return render_template('9-states.html', all_states=all_states)


@app.route('/states/<id>', strict_slashes=False)
def display_States(id):
    """ Renders state with its cities based on id"""
    states = storage.all(State).values()
    state = 0
    for instance in states:
        if id == instance.id:
            state = instance
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def refresh_session(exception):
    """ for every request it will close the session and refesh """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
