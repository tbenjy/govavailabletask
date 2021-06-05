from HotChairs.Classes.Mongo_Base import *


# Constant words of fields' names
ID_FLD = "id"
NAME_FLD = "name"


class Organizations(MongoBase):
    def __init__(self):
        super().__init__(db=HOTCHAIRS_DB, collection=ORGANIZATIONS_COL)
        # Fills the collection with documents only once in the first time
        if len(list(self._collection.find())) == 0:
            self.organizations_filling()

    def organizations_filling(self):
        self._collection.insert_one(
            {ID_FLD: self._get_id(), NAME_FLD: "ממשל זמין"}
        )
        self._collection.insert_one(
            {ID_FLD: self._get_id(), NAME_FLD: "משרד החוץ"}
        )
        self._collection.insert_one(
            {ID_FLD: self._get_id(), NAME_FLD: "אגד"}
        )
        self._collection.insert_one(
            {ID_FLD: self._get_id(), NAME_FLD: "דואר ישראל"}
        )
        self._collection.insert_one(
            {ID_FLD: self._get_id(), NAME_FLD: "פעמונים"}
        )

    def get_all_organizations(self):
        # Selects all the organizations
        return json_util.dumps(
            self._collection.find().sort(
                NAME_FLD, pymongo.ASCENDING
            )
        )
