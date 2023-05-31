import getpass
import pymongo
from pymongo import MongoClient

class Utilities:
    @staticmethod
    def startup():
        cluster = "MONGODB CONNECTION STRING"
        client = MongoClient(cluster)
        db = client.Phase3
        return db
    @staticmethod
    def get_size(db,size_name):
        result = db.sizes.find_one({"name": size_name})['_id']
        return result