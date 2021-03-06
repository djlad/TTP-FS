from flask import Blueprint
from flask_user import login_required, current_user
from flask import Flask, request, render_template_string, render_template
from flask import request

from services import get_stock
from services.transaction import make_purchase, sum_transactions

login_routes = Blueprint('login_routes', __name__, template_folder='templates')

@login_routes.route('/')
@login_required
def stocks_page(transaction_message=""):
    holdings = sum_transactions(current_user.id)
    quotes = []
    for holding in holdings:
        quotes.append(get_stock.get_stock(holding.symbol))
    return render_template('stocks.html',
                           user=current_user, 
                           holdings=holdings, 
                           quotes=quotes,
                           transaction_message=transaction_message)

@login_routes.route('/fuser')
def index():
    return render_template_string("""
            {% extends "flask_user_layout.html" %}
            {% block content %}
                <h2>{%trans%}Home page{%endtrans%}</h2>
                <p><a href={{ url_for('user.register') }}>{%trans%}Register{%endtrans%}</a></p>
                <p><a href={{ url_for('user.login') }}>{%trans%}Sign in{%endtrans%}</a></p>
                <p><a href={{ url_for('user.logout') }}>{%trans%}Sign out{%endtrans%}</a></p>
            {% endblock %}
            """)

@login_routes.route('/buy', methods=["POST"])
@login_required
def buy_stock():
    '''
    Endpoint for making a purchase for a user
    '''
    quantity = request.form['quantity']
    ticker = request.form['symbol'].upper()
    message = make_purchase(ticker, quantity, current_user.id)

    if not message:
        message = "Purchase Successful"
    else:
        message = "Purchase Failed: " + message
    
    if "render" in request.form:
        return stocks_page(message)
    
    return message
