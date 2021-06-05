from django.conf import settings
from bson import json_util
from HotChairs.Constant_Words import *
import pymongo


class MongoBase:
    def __init__(self, db, collection):
        self.__client = pymongo.MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        self._db = self.__client[db]
        self._collection = self._db[collection]

    # Gets the next ID of the collection
    def _get_id(self):
        name = self._collection.name
        if not self._db.sequences.find_one(dict(name=name)):
            self._db.sequences.insert_one(dict(name=name, next_id=1))
            return 0
        else:
            sq = self._db.sequences.find_one_and_update({"name": name}, {"$inc": {"next_id": 1}})
            return sq['next_id']
