from pymongo import MongoClient

from sample_project import settings


_client = None


def get_mongo_client():
    global _client
    if _client is None:
        _client = MongoClient(host=settings.MONGO_HOST, port=settings.MONGO_PORT)

    return _client


def get_mongo_db():
    return get_mongo_client()[settings.MONGO_DATABASE]
