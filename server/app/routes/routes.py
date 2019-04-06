from flask import Blueprint
from flask_user import login_required, current_user
from flask import Flask, request, render_template_string, render_template

from services import get_stocks

login_routes = Blueprint('login_routes', __name__, template_folder='templates')

@login_routes.route('/stocks')
@login_required
def stocks_page():
    print('login route')
    print(current_user)
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
