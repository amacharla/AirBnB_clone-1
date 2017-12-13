#!/usr/bin/python3
""" Using Flask and rendering content """

from web_flask import app

@app.route('/', strict_slashes=False)
def index():
    """ renders when no uri is requested """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def display_HBNB():
    """ renders if uri /hbhb is requested HBNB """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def display_variable(text):
    """ renders variable and replaces underscore with space """
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
