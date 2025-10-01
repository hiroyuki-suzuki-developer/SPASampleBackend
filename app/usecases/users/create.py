from schemas.request.users.createUser import CreateUser
from repositories.userRepository import create_user
from sqlalchemy.orm import Session

def create_user_usecase(db: Session, user: CreateUser):
    return create_user(db, user)
