from app import app
from flask_script import Server, Manager
from flask_migrate import Migrate, MigrateCommand
from models.database import db

#manager.add_command('db', MigrateCommand)
manager = Manager(app, Server())

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__=="__main__":
    manager.run()