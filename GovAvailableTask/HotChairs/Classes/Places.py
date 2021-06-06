from HotChairs.Classes.Mongo_Base import MongoBase
from HotChairs.Constant_Words import *
import pymongo

# Constant words of fields' names
ID_FLD = "id"
NAME_FLD = "name"
ORGANIZATION_FLD = "organization"
CATCH_BY_FLD = "catchBy"


class Places(MongoBase):
    def __init__(self):
        super().__init__(db=HOTCHAIRS_DB, collection=PLACES_COL)
        # Fills the collection with documents only once in the first time
        if len(list(self._collection.find())) == 0:
            self.places_filling()

    def places_filling(self):
        self._collection.insert_one(
            {ID_FLD: self._get_id(), NAME_FLD: "קומה 1, פינה ימנית", ORGANIZATION_FLD: 0, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {ID_FLD: self._get_id(), NAME_FLD: "קומה 2, חדר שני מימין", ORGANIZATION_FLD: 0, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {ID_FLD: self._get_id(), NAME_FLD: "קומה 1, צפון-מערב", ORGANIZATION_FLD: 0, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {ID_FLD: self._get_id(), NAME_FLD: "קומה 3, מעבר", ORGANIZATION_FLD: 0, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {ID_FLD: self._get_id(), NAME_FLD: "קומה 2, חדר ראשון משמאל", ORGANIZATION_FLD: 0, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {ID_FLD: self._get_id(), NAME_FLD: "עמדת מזכירות", ORGANIZATION_FLD: 1, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {ID_FLD: self._get_id(), NAME_FLD: "חדר מנכ\"ל", ORGANIZATION_FLD: 1, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {ID_FLD: self._get_id(), NAME_FLD: "חדר גזבר", ORGANIZATION_FLD: 1, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {ID_FLD: self._get_id(), NAME_FLD: "חדר ישיבות", ORGANIZATION_FLD: 2, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {ID_FLD: self._get_id(), NAME_FLD: "חדר אוכל", ORGANIZATION_FLD: 2, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {ID_FLD: self._get_id(), NAME_FLD: "שורה 3, מחשב 8", ORGANIZATION_FLD: 3, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {ID_FLD: self._get_id(), NAME_FLD: "שורה 5, מחשב 1", ORGANIZATION_FLD: 3, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {ID_FLD: self._get_id(), NAME_FLD: "שורה 5, מחשב 5", ORGANIZATION_FLD: 3, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {ID_FLD: self._get_id(), NAME_FLD: "שורה 10, מחשב 7", ORGANIZATION_FLD: 3, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {ID_FLD: self._get_id(), NAME_FLD: "עמדת שמירה - בניין", ORGANIZATION_FLD: 4, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {ID_FLD: self._get_id(), NAME_FLD: "עמדת שמירה - חניון", ORGANIZATION_FLD: 4, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {ID_FLD: self._get_id(), NAME_FLD: "עמדת שמירה - קומה 4", ORGANIZATION_FLD: 4, CATCH_BY_FLD: -1}
        )
        self._collection.insert_one(
            {ID_FLD: self._get_id(), NAME_FLD: "עמדת שמירה - קומה 2", ORGANIZATION_FLD: 4, CATCH_BY_FLD: -1}
        )

    def get_place_by_id(self, place_id):
        # Selects the place by the id
        return list(
            self._collection.find(
                {ID_FLD: place_id}
            )
        )

    def get_places_by_organization(self, organization_id):
        # Selects the places of the organizations and sorts them by names
        return list(
            self._collection.find(
                {ORGANIZATION_FLD: organization_id}
            ).sort(
                NAME_FLD, pymongo.ASCENDING
            )
        )

    def get_place_by_employee(self, employee_id):
        # Selects the current place of the employee
        return list(
            self._collection.find(
                {CATCH_BY_FLD: employee_id}
            )
        )
