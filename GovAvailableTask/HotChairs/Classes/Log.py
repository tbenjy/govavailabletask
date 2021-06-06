from datetime import datetime
from HotChairs.Classes.Mongo_Base import MongoBase
from HotChairs.Constant_Words import *


class Log(MongoBase):
	def __init__(self):
		super().__init__(db=HOTCHAIRS_DB, collection=LOG_COL)

	def add_message(self, level, message):
		# Adds the message to the table
		self._collection.insert_one(
			{"id": self._get_id(), "dateTime": datetime.now().strftime("%Y-%m-%d, %H:%M:%S"), "level": level, "message": message}
		)
