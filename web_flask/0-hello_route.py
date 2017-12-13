#!/usr/bin/python3
""" creating Index with returns "Hello HBNB!" when requested """

from web_flask import app

@app.route('/', strict_slashes=False)
def index():
    """ renders Hello HBNB! """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
