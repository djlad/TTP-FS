from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .database import db

'''
class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)

    def __init__(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()'''