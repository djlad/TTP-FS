from flask import Blueprint
from flask_user import login_required, current_user
from flask import Flask, request, render_template_string, render_template
from flask import request

from services import get_stock
from services.make_transaction import make_purchase

login_routes = Blueprint('login_routes', __name__, template_folder='templates')

@login_routes.route('/stocks')
@login_required
def stocks_page():
    print('login route')
    print(get_stock.get_stock("aapl"))
    return render_template('stocks.html', user=current_user)

@login_routes.route('/')
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
    quantity = request.form['quantity']
    ticker = request.form['symbol']
    success = make_purchase(ticker, quantity, current_user.id)

    if success:
        return "purchase successful"
    else:
        return "purchase failed"
