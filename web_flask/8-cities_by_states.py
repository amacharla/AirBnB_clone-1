#!/usr/bin/python3
""" Using Flask and rendering all States"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def display_States():
    """ Requests list of all cities by state """
    all_states = storage.all(State).values()
    return render_template('8-cities_by_states.html', all_states=all_states)


@app.teardown_appcontext
def refresh_session(exception):
    """ for every request it will close the session and refesh """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
