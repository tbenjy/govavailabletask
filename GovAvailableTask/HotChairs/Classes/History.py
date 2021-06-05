from HotChairs.Classes.Mongo_Base import *


# Constant words of fields' names
ID_FLD = "id"
EMPLOYEE_FLD = "employee"
PLACE_FLD = "place"
RESERVATION_TIME_FLD = "ReservationTime"


class History(MongoBase):
    def __init__(self):
        super().__init__(db=HOTCHAIRS_DB, collection=HISTORY_COL)
