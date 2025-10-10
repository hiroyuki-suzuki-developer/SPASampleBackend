from models.users import User
from sqlalchemy.orm import Session
from sqlalchemy import select
from schemas.request.auth.register import Register
import bcrypt

def index_user(db: Session):
    stmt = select(User).order_by(User.id)
    result = db.execute(stmt)
    users = result.scalars().all()
    return users

def get_user(db: Session, user_id: int):
    stmt = select(User).filter(User.id == user_id)
    result = db.execute(stmt)
    user = result.scalar_one_or_none()
    return user

def get_user_by_email(db: Session, email: str):
    stmt = select(User).filter(User.email == email)
    result = db.execute(stmt)
    user = result.scalar_one_or_none()
    return user

def create_user(db: Session, user: Register):
    user_data_dict = user.model_dump()
    password_bytes = user_data_dict.get('password', '').encode('utf-8')
    salt = bcrypt.gensalt(rounds=12)
    hashed_bytes = bcrypt.hashpw(password_bytes, salt)
    user_data_dict['password'] = hashed_bytes.decode('utf-8')
    db_user = User(**user_data_dict)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return user


def update_user(db: Session, user_id: int, user: User):
    stmt = select(User).filter(User.id == user_id)
    result = db.execute(stmt)
    user = result.scalar_one_or_none()
    user.update(user)
    db.commit()
    return user

def delete_user(db: Session, user_id: int):
    stmt = select(User).filter(User.id == user_id)
    result = db.execute(stmt)
    user = result.scalar_one_or_none()
    user.delete()
    db.commit()
    return user
