from fastapi import APIRouter, Depends
import os
from sqlalchemy.orm import Session
from repositories.userRepository import index_user, get_user, get_user_by_email, create_user, update_user, delete_user
from usecases.users.index import index_user_usecase
from usecases.users.detail import detail_user_usecase
from usecases.users.create import create_user_usecase
from schemas.request.users.createUser import CreateUser
from database import get_db

router = APIRouter()

@router.get('/users')
def users(db: Session = Depends(get_db)):
    try:
        users = index_user_usecase(db)
    except Exception as e:
        return {'error': str(e)}
    return {'users': users}

@router.get('/users/{user_id}')
def user(user_id: int, db: Session = Depends(get_db)):
    try:
        user = detail_user_usecase(db, user_id)
    except Exception as e:
        return {'error': str(e)}
    return {'user': user}

@router.post('/users')
def create_user(user: CreateUser = Depends(CreateUser), db: Session = Depends(get_db)):
    try:
        user = create_user_usecase(db, user)
    except Exception as e:
        return {'error': str(e)}
