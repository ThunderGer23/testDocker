# Connecting to the MongoDB database.
from pymongo import MongoClient
from os import environment as env

conn = MongoClient(env['DOCKER'])
