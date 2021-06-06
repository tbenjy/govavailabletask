from HotChairs.Classes.Mongo_Base import MongoBase
from HotChairs.Classes.Places import Places
from HotChairs.Constant_Words import *
import pymongo


class History(MongoBase):
    def __init__(self):
        super().__init__(db=HOTCHAIRS_DB, collection=HISTORY_COL)

    def get_history_by_employee(self, employee_id):
        return list(
            self._collection.find(
                {HISTORY_EMPLOYEE_FLD: employee_id}
            )
        )

    @staticmethod
    def get_history_place(history_row):
        places = Places()
        history_place = places.get_place_by_id(history_row[HISTORY_PLACE_FLD])
        return {HISTORY_PLACE_NAME_FLD: history_place[0]["name"]}
