from bson import json_util
from HotChairs.Classes.Mongo_Base import *
from HotChairs.Constant_Words import *

# Constant words of fields' names
ID_FLD = "id"
NAME_FLD = "name"
ORGANIZATION_FLD = "organization"
CATCH_BY_FLD = "catchBy"


class Places(MongoBase):
    def __init__(self):
        super().__init__(db=HOTCHAIRS_DB, collection=PLACES_COL)
