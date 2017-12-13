#!/usr/bin/python3
""" Using Flask and rendering content """

from web_flask import app
from flask import render_template

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

@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_variable_with_defaults(text):
    """ renders variable else defaults to 'is cool' """
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:num>', strict_slashes=False)
def display_variable_int(num):
    """ renders only int variable """
    return '{:n} is a number'.format(num)

@app.route('/number_template/<int:num>', strict_slashes=False)
def display_variable_HTML(num):
    """ renders html content only int variable """
    return render_template('5-number.html', number=num)

@app.route('/number_odd_or_even/<int:num>', strict_slashes=False)
def display_variable_HTML_oddOrEven(num):
    """ renders html content only int variable """
    return render_template('6-number_odd_or_even.html', number=num)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
