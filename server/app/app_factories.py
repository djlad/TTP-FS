import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager
from flask_mail import Mail, Message

from routes.routes import login_routes
from models.database import db
from models.usermodel import UserModel
from models.transaction import Transaction


from flask_user.forms import RegisterForm
from wtforms import StringField
from wtforms.validators import DataRequired

class NameRegisterForm(RegisterForm):
    name = StringField('name', validators=[DataRequired('First name is required')])

class NameUserManager(UserManager):
    def customize(self, app):
        # Configure customized forms
        self.RegisterFormClass = NameRegisterForm


def create_app_db(db, test_config=""):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # load the instance config, if it exists, when not testing
    #app.config.from_pyfile('config.py', silent=True)
    if not test_config:
        app.config.from_object("config.DefaultConfig")
    else:
        app.config.from_object(test_config)
    #mail = Mail(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #format database connection uri
    db_user = app.config['DB_USER']
    db_password = app.config['DB_PASSWORD']
    db_url = app.config['DB_URL']
    db_name = app.config['DB_NAME']

    #connect to database using flask's sql alchemy
    #sqlalchemyuri = f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}'
    sqlalchemyuri  = 'postgresql://'+db_user+':'+db_password+'@'+db_url+'/'+db_name
    app.config['SQLALCHEMY_DATABASE_URI'] = sqlalchemyuri


    #bind datbase to this app
    db.init_app(app)
    app.app_context().push()
    
    #initialize flask user for authentication
    #user_manager = UserManager(app, db, UserModel) #register_form=nameRegisterForm)
    user_manager = NameUserManager(app, db, UserModel) #register_form=nameRegisterForm)
    

    #initialize database
    #try:
    #    db.drop_all()
    #except:
    #    print("couldn't drop")
    #    pass

    db.create_all()
    #addTransaction(db, 0)


    #add routes
    app.register_blueprint(login_routes)

    return app

def create_app_test(test_config):
    return create_app_db(db, test_config)