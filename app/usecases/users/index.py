from repositories.userRepository import index_user, create_user
from sqlalchemy.orm import Session
from models.users import User

def index_user_usecase(db: Session):
    return index_user(db)
