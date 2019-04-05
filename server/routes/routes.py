from flask import Blueprint
from flask_user import login_required

login_routes = Blueprint('login_routes', __name__, template_folder='templates')
@login_routes.route('/login')
@login_required
def login():
    return "hello"

@login_routes.route('/')
def index():
    return "welcome"