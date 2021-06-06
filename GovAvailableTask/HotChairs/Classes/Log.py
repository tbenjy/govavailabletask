from bson import json_util
from HotChairs.Classes.Mongo_Base import *
from HotChairs.Constant_Words import *


# Constant words of fields' names
ID_FLD = "id"
EMPLOYEE_FLD = "employee"
LEVEL_FLD = "level"
MESSAGE_FLD = "message"


class Log(MongoBase):
	def __init__(self):
		super().__init__(db=HOTCHAIRS_DB, collection=LOG_COL)

	def add_message(self, level, message):
		self._collection.insert_one(
			{"id": self._get_id(), "dateTime": datetime.now().strftime("%Y-%m-%d, %H:%M:%S"), "level": level, "message": message}
		)
