# coding=utf-8

from sqlalchemy import Column, String

from .model import Model

from flask_user import UserMixin
from .database import db


class UserModel(Model, UserMixin):
    __tablename__ = 'user'

    # User Authentication fields
    email = db.Column(db.String(255), nullable=False, unique=True)
    email_confirmed_at = db.Column(db.DateTime())
    password = db.Column(db.String(255), nullable=False)

    # User fields
    active = db.Column(db.Boolean()),