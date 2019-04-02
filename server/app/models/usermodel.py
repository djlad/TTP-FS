# coding=utf-8

from sqlalchemy import Column, String

from .model import Model, Base


class UserModel(Model, Base):
    __tablename__ = 'user'

    title = Column(String)
    description = Column(String)

    def __init__(self, email, password):
        Model.__init__(self)
        self.email = email
        self.password = password