from datetime import datetime
from HotChairs.Classes.Mongo_Base import MongoBase
from HotChairs.Classes.Places import Places
from HotChairs.Constant_Words import *


class History(MongoBase):
    def __init__(self):
        super().__init__(db=HOTCHAIRS_DB, collection=HISTORY_COL)

    def get_history_by_employee(self, employee_id):
        # Selects all the histories of the employee
        return list(
            self._collection.find(
                {HISTORY_EMPLOYEE_FLD: employee_id}
            )
        )

    @staticmethod
    def get_place_name_of_history(history_row):
        # Finds the name of the history's place
        places = Places()
        history_place = places.get_place_by_id(history_row[HISTORY_PLACE_FLD])
        return {HISTORY_PLACE_NAME_FLD: history_place[0]["name"]}

    def insert_new_place_of_employee(self, employee_id, place_id):
        # Adds the reservation to the history
        self._collection.insert_one(
            {HISTORY_ID_FLD: self._get_id(), HISTORY_EMPLOYEE_FLD: employee_id, HISTORY_PLACE_FLD: place_id, RESERVATION_TIME_FLD: datetime.now().strftime("%Y-%m-%d, %H:%M:%S")}
        )
