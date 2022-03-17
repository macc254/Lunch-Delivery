from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User, Order, Meal
from .. import db, photos
from flask_login import login_required, current_user



@main.route('/')
def index():
    
    return render_template('home.html', name='')

@main.route('/checkout')
@login_required
def checkout():
    title='Checkout'
    return render_template('checkout.html', title=title)


    

@main.route('/get_totals')
def get_totals():
    pass
def add_order():
    pass

@main.route('/restaurant')
def restaurants():

    return render_template('restaurant.html')


@main.route('/menu')
def menu():
    return render_template('menue.html')
