from app_factories import create_app_db
from models.database import db

app = create_app_db(db)