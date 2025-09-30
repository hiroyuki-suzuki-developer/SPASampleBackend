from fastapi import APIRouter
import os

router = APIRouter()

@router.get('/users')
def users():
    return {'users': 'users'}

@router.get('/users/{user_id}')
def user(user_id: int):
    return {'user_id': user_id}

@router.post('/users')
def create_user():
    return {'user': user}
