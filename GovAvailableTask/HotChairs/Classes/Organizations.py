from HotChairs.Classes.Mongo_Base import MongoBase
from HotChairs.Constant_Words import *
import pymongo


class Organizations(MongoBase):
    def __init__(self):
        super().__init__(db=HOTCHAIRS_DB, collection=ORGANIZATIONS_COL)
        # Fills the collection with documents only once in the first time
        if len(list(self._collection.find())) == 0:
            self.organizations_filling()

    def organizations_filling(self):
        self._collection.insert_one(
            {ORGANIZATION_ID_FLD: self._get_id(), ORGANIZATION_NAME_FLD: "ממשל זמין"}
        )
        self._collection.insert_one(
            {ORGANIZATION_ID_FLD: self._get_id(), ORGANIZATION_NAME_FLD: "משרד החוץ"}
        )
        self._collection.insert_one(
            {ORGANIZATION_ID_FLD: self._get_id(), ORGANIZATION_NAME_FLD: "אגד"}
        )
        self._collection.insert_one(
            {ORGANIZATION_ID_FLD: self._get_id(), ORGANIZATION_NAME_FLD: "דואר ישראל"}
        )
        self._collection.insert_one(
            {ORGANIZATION_ID_FLD: self._get_id(), ORGANIZATION_NAME_FLD: "פעמונים"}
        )

    def get_all_organizations(self):
        # Selects all the organizations
        return list(
            self._collection.find().sort(
                ORGANIZATION_NAME_FLD, pymongo.ASCENDING
            )
        )
