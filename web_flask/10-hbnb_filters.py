#!/usr/bin/python3
""" Using Flask and rendering all States for hbnb"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def display_States_Amenity():
    """ Renders all states and amenities for hbnb """
    all_states = storage.all(State).values()
    all_amenity = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', all_states=all_states,
                           all_amenity=all_amenity)


@app.teardown_appcontext
def refresh_session(exception):
    """ for every request it will close the session and refesh """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
