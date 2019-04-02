from flask import Blueprint

login_routes = Blueprint('login_routes', __name__, template_folder='templates')
@login_routes.route('/login')
def login():
    return "hello"