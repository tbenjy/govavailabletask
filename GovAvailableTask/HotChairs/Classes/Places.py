from HotChairs.Classes.Mongo_Base import MongoBase
from HotChairs.Constant_Words import *
import pymongo


class Places(MongoBase):
    def __init__(self):
        super().__init__(db=HOTCHAIRS_DB, collection=PLACES_COL)
        # Fills the collection with documents only once in the first time
        if len(list(self._collection.find())) == 0:
            self.places_filling()

    def places_filling(self):
        self._collection.insert_one(
            {PLACE_ID_FLD: self._get_id(), PLACE_NAME_FLD: "קומה 1, פינה ימנית", PLACE_ORGANIZATION_FLD: 0, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {PLACE_ID_FLD: self._get_id(), PLACE_NAME_FLD: "קומה 2, חדר שני מימין", PLACE_ORGANIZATION_FLD: 0, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {PLACE_ID_FLD: self._get_id(), PLACE_NAME_FLD: "קומה 1, צפון-מערב", PLACE_ORGANIZATION_FLD: 0, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {PLACE_ID_FLD: self._get_id(), PLACE_NAME_FLD: "קומה 3, מעבר", PLACE_ORGANIZATION_FLD: 0, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {PLACE_ID_FLD: self._get_id(), PLACE_NAME_FLD: "קומה 2, חדר ראשון משמאל", PLACE_ORGANIZATION_FLD: 0, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {PLACE_ID_FLD: self._get_id(), PLACE_NAME_FLD: "עמדת מזכירות", PLACE_ORGANIZATION_FLD: 1, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {PLACE_ID_FLD: self._get_id(), PLACE_NAME_FLD: "חדר מנכ\"ל", PLACE_ORGANIZATION_FLD: 1, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {PLACE_ID_FLD: self._get_id(), PLACE_NAME_FLD: "חדר גזבר", PLACE_ORGANIZATION_FLD: 1, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {PLACE_ID_FLD: self._get_id(), PLACE_NAME_FLD: "חדר ישיבות", PLACE_ORGANIZATION_FLD: 2, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {PLACE_ID_FLD: self._get_id(), PLACE_NAME_FLD: "חדר אוכל", PLACE_ORGANIZATION_FLD: 2, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {PLACE_ID_FLD: self._get_id(), PLACE_NAME_FLD: "שורה 3, מחשב 8", PLACE_ORGANIZATION_FLD: 3, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {PLACE_ID_FLD: self._get_id(), PLACE_NAME_FLD: "שורה 5, מחשב 1", PLACE_ORGANIZATION_FLD: 3, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {PLACE_ID_FLD: self._get_id(), PLACE_NAME_FLD: "שורה 5, מחשב 5", PLACE_ORGANIZATION_FLD: 3, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {PLACE_ID_FLD: self._get_id(), PLACE_NAME_FLD: "שורה 10, מחשב 7", PLACE_ORGANIZATION_FLD: 3, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {PLACE_ID_FLD: self._get_id(), PLACE_NAME_FLD: "עמדת שמירה - בניין", PLACE_ORGANIZATION_FLD: 4, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {PLACE_ID_FLD: self._get_id(), PLACE_NAME_FLD: "עמדת שמירה - חניון", PLACE_ORGANIZATION_FLD: 4, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {PLACE_ID_FLD: self._get_id(), PLACE_NAME_FLD: "עמדת שמירה - קומה 4", PLACE_ORGANIZATION_FLD: 4, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {PLACE_ID_FLD: self._get_id(), PLACE_NAME_FLD: "עמדת שמירה - קומה 2", PLACE_ORGANIZATION_FLD: 4, CATCH_BY_FLD: -1}
        )

    def get_place_by_id(self, place_id):
        # Selects the place by the id
        return list(
            self._collection.find(
                {PLACE_ID_FLD: place_id}
            )
        )

    def get_places_by_organization(self, organization_id):
        # Selects the places of the organization and sorts them by names
        return list(
            self._collection.find(
                {PLACE_ORGANIZATION_FLD: organization_id}
            ).sort(
                PLACE_NAME_FLD, pymongo.ASCENDING
            )
        )

    def get_place_by_employee(self, employee_id):
        # Selects the current place of the employee
        return list(
            self._collection.find(
                {CATCH_BY_FLD: employee_id}
            )
        )

    def get_free_places_by_organization(self, organization_id):
        # Selects the free places of the organization and sorts them by names
        return list(
            self._collection.find(
                {PLACE_ORGANIZATION_FLD: organization_id, CATCH_BY_FLD: -1}
            ).sort(
                PLACE_NAME_FLD, pymongo.ASCENDING
            )
        )

    def update_employee_of_the_place(self, place_id, employee_id):
        # Updates the current employee of the place
        self._collection.update_one({PLACE_ID_FLD: place_id}, {"$set": {CATCH_BY_FLD: employee_id}})
