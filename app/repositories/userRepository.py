from models.users import User
from sqlalchemy.orm import Session
from sqlalchemy import select


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

def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
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
