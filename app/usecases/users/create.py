from schemas.request.users.createUser import CreateUser

def create_user_usecase(user: CreateUser):
    return {
        'id': 1,
        'name': user.name,
        'email': user.email,
        'password': user.password,
        'gender': user.gender
    }
