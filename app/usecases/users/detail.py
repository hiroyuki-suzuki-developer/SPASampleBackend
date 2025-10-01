from repositories.userRepository import get_user
from sqlalchemy.orm import Session

def detail_user_usecase(db: Session, user_id: int):
    return get_user(db, user_id)
