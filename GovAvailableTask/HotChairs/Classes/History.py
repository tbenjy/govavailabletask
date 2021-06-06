from bson import json_util
from HotChairs.Classes.Mongo_Base import *
from HotChairs.Constant_Words import *


# Constant words of fields' names
ID_FLD = "id"
DATE_TIME_FLD = "dateTime"
PLACE_FLD = "place"
RESERVATION_TIME_FLD = "ReservationTime"


class History(MongoBase):
    def __init__(self):
        super().__init__(db=HOTCHAIRS_DB, collection=HISTORY_COL)
