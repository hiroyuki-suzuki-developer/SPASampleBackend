from repositories.userRepository import get_user
from sqlalchemy.orm import Session
from schemas.request.auth.login import Login
from repositories.userRepository import get_user_by_email
import bcrypt

def login_usecase(db: Session, user: Login):
    db_user = get_user_by_email(db, user.email)
    if not db_user:
        raise Exception('認証に失敗しました。')
    password_bytes = user.password.encode('utf-8')
    hashed_bytes = db_user.password.encode('utf-8')
    if bcrypt.checkpw(password_bytes, hashed_bytes):
        return db_user
        # token = 'jsw'
        # return {'token': token}
    else:
        raise Exception('認証に失敗しました。')
