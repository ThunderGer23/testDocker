# Connecting to the MongoDB database.
from pymongo import MongoClient
from os import environ as env

conn = MongoClient(env['MONGO_CLI'])
