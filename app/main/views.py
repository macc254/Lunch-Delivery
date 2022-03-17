from flask import render_template,url_for
from . import main

@main.route('/')
def restaurant():

    return render_template('restaurants.html')

@main.route('/menu')
def menu():

    return render_template('menus.html')