from pymongo import MongoClient


def get_mongo_client():
    # todo change to env variable
    return MongoClient("mongodb://root:mongo@localhost:27017/")
