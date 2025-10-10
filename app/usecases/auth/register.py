from schemas.request.auth.register import Register
from repositories.userRepository import create_user
from sqlalchemy.orm import Session

def create_user_usecase(db: Session, user: Register):
    return create_user(db, user)
