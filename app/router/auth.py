from fastapi import APIRouter, Depends
import os
from sqlalchemy.orm import Session
from repositories.userRepository import index_user, get_user, get_user_by_email, create_user, update_user, delete_user
from usecases.auth.register import create_user_usecase
from schemas.request.auth.register import Register
from schemas.request.auth.login import Login
from database import get_db
from usecases.auth.login import login_usecase

router = APIRouter()

@router.post('/login')
def login(user: Login, db: Session = Depends(get_db)):
    try:
        user = login_usecase(db, user)
        return user
    except Exception as e:
        return {'error': str(e)}

@router.post('/register')
def register(user: Register, db: Session = Depends(get_db)):
    try:
        user = create_user_usecase(db, user)
    except Exception as e:
        return {'error': str(e)}
