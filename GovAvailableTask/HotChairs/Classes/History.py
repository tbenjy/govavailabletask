from HotChairs.Classes.Mongo_Base import MongoBase
from HotChairs.Classes.Places import Places
from HotChairs.Constant_Words import *
import pymongo


# Constant words of fields' names
ID_FLD = "id"
EMPLOYEE_FLD = "employee"
PLACE_FLD = "place"
RESERVATION_TIME_FLD = "ReservationTime"

PLACE_NAME_FLD = "placeName"


class History(MongoBase):
    def __init__(self):
        super().__init__(db=HOTCHAIRS_DB, collection=HISTORY_COL)

    def get_history_by_employee(self, employee_id):
        return list(
            self._collection.find(
                {EMPLOYEE_FLD: employee_id}
            )
        )

    @staticmethod
    def get_history_place(history_row):
        places = Places()
        history_place = places.get_place_by_id(history_row[PLACE_FLD])
        return {PLACE_NAME_FLD: history_place[0]["name"]}
