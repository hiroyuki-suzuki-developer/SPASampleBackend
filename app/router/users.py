from fastapi import APIRouter, Depends
import os
from sqlalchemy.orm import Session

from usecases.users.index import index_user_usecase
from usecases.users.detail import detail_user_usecase
from usecases.users.create import create_user_usecase
from schemas.request.users.createUser import CreateUser

router = APIRouter()

@router.get('/users')
def users():
    try:
        users = index_user_usecase()
    except Exception as e:
        return {'error': str(e)}
    return {'users': users}

@router.get('/users/{user_id}')
def user(user_id: int):
    try:
        user = detail_user_usecase(user_id)
    except Exception as e:
        return {'error': str(e)}
    return {'user': user}

@router.post('/users')
def create_user(user: CreateUser = Depends(CreateUser)):
    try:
        user = create_user_usecase(user)
    except Exception as e:
        return {'error': str(e)}
