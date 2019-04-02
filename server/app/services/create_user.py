from models.model import Session, engine, Base
from models.usermodel import UserModel

Base.metadata.create_all(engine)

def create_user():
    session = Session()
    newUser = UserModel("username1", "password1")
    session.add(newUser)
    session.commit()
    users = session.query(UserModel).all()
    print(users)


if __name__ == '__main__':
    create_user()