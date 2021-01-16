from mongoengine import connect, Q
import os

MONGODB_URL = os.getenv('MONGODB_URL')

class MongoDbAcess(object):
    def __init__(self) -> None:
        connect('bitcoin', host=MONGODB_URL)