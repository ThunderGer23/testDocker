from fastapi import APIRouter
from config.db import conn
from schemas.user import userEntity, usersEntity
from models.user import User

user = APIRouter()

@user.get('/users')
def search_users():
    return usersEntity(conn.local.user.find())

@user.get('/user/{id}')
def search_user():
    return "Holi :v"

@user.post('/user')
def create_user(user: User):
    new_user = dict(user)
    id = conn.local.user.insert_one(new_user).inserted_id
    return str(id)

@user.put('/user/{id}')
def update_user():
    return "Holi :v"

@user.delete('/user/{id}')
def delete_user():
    return "Holi :v"