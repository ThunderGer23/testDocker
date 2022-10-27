from fastapi import APIRouter

user = APIRouter()

@user.get('/users')
def search_users():
    return "Holi :v"

@user.get('/user/{id}')
def search_user():
    return "Holi :v"

@user.post('/user')
def create_user():
    return "Holi :v"

@user.put('/user/{id}')
def update_user():
    return "Holi :v"

@user.delete('/user/{id}')
def delete_user():
    return "Holi :v"