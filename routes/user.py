from fastapi import APIRouter, Response
from config.db import conn
from schemas.user import userEntity, usersEntity
from models.user import User
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_226_IM_USED


user = APIRouter()

@user.get('/users', response_model=list[User], tags=["Users"])
def search_users():
    """
    It returns a list of users from the database
    :return: A list of users
    """
    return usersEntity(conn.local.user.find())

@user.get('/user/{id}', response_model = User, tags=["Users"])
def search_user(id: str):
    """
    It takes a string as an argument, converts it to an ObjectId, and then searches the database for a
    user with that id
    
    :param id: str
    :type id: str
    :return: A userEntity object
    """
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))

@user.post('/user', response_model=User, tags=["Users"])
def create_user(user: User):
    """
    It takes a user object, creates a new user object, encrypts the password, deletes the id, inserts
    the new user object into the database, and returns the new user object
    
    :param user: User
    :type user: User
    :return: A userEntity object
    """
    new_user = dict(user)
    new_user['password'] = sha256_crypt.encrypt(new_user['password'])
    del new_user['id']
    id = conn.local.user.insert_one(new_user).inserted_id
    user = conn.local.user.find_one({"_id" : id})
    return userEntity(user)

@user.put('/user/{id}', response_model=list[User], tags=["Users"])
def update_user(id: str, user: User):
    """
    It takes a user object, checks if the password is empty, if it is, it sets the password to the last
    password, if it isn't, it encrypts the password and sets it to the new password
    
    :param id: str
    :type id: str
    :param user: User
    :type user: User
    :return: A list of users
    """
    new_user = dict(user)
    conn.local.user.find_one_and_update({"_id": ObjectId(id)}, {"$set": new_user})
    return userEntity(conn.local.user.find_one({"_id" : ObjectId(id)}))

@user.delete('/user/{id}', status_code = HTTP_226_IM_USED, tags=["Users"])
def delete_user(id: str):
    """
    It deletes a user from the database and returns a response with a status code of 226
    
    :param id: str - the id of the user to delete
    :type id: str
    :return: The response object
    """
    userEntity(conn.local.user.find_one_and_delete({'_id': ObjectId(id)}))
    return Response(status_code= HTTP_226_IM_USED)