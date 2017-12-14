#!/usr/bin/python3
"""Using Flask"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ renders when no uri is requested """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_HBNB():
    """ renders if uri /hbhb is requested HBNB """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
