# coding=utf-8

from sqlalchemy import Column, String

#from .model import Model

from flask_user import UserMixin
from .database import db

#from .transaction import Transaction


class UserModel(db.Model, UserMixin):
    __tablename__ = 'app_user'
    id = db.Column(db.Integer, primary_key=True)

    # User Authentication fields
    email = db.Column(db.String(255), nullable=False, unique=True)
    email_confirmed_at = db.Column(db.DateTime())
    password = db.Column(db.String(255), nullable=False)

    # User fields
    active = db.Column(db.Boolean())
    name = db.Column(db.String(50), default='')

    # App specific fields
    # Web Stocks App:
    balance = db.Column(db.Float, nullable=True, default=5000.0)
    currency_type = db.Column(db.String(10), nullable=True, default="USD")

    #relationships
    transactions = db.relationship("Transaction", backref="UserModel")