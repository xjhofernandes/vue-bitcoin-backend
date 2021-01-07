from mongoengine import connect, Q
import os

USERNAME_MONGO = os.getenv('USERNAME_MONGO')
PASSWORD_MONGO = os.getenv('PASSWORD_MONGO')
CLUSTER_MONGO = os.getenv('CLUSTER_MONGO')
DATABASE_MONGO = os.getenv('CLUSTER_MONGO')

class MongoDbAcess(object):
    def __init__(self) -> None:
        #connect('bitcoin', host=f"mongodb+srv://{USERNAME_MONGO}:{PASSWORD_MONGO}@{CLUSTER_MONGO}.mongodb.net/{DATABASE_MONGO}?retryWrites=true&w=majority")
        connect('bitcoin', host=f"mongodb+srv://admin:bitadmin@cluster0.oyaw3.mongodb.net/bitcoin?retryWrites=true&w=majority")