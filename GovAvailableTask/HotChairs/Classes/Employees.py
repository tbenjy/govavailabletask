from HotChairs.Classes.Mongo_Base import MongoBase
from HotChairs.Classes.Places import Places
from HotChairs.Constant_Words import *
import pymongo


class Employees(MongoBase):
    def __init__(self):
        super().__init__(db=HOTCHAIRS_DB, collection=EMPLOYEES_COL)
        # Fills the collection with documents only once in the first time
        if len(list(self._collection.find())) == 0:
            self.employees_filling()

    def employees_filling(self):
        self._collection.insert_one(
            {EMPLOYEE_ID_FLD: self._get_id(), IDENTITY_CARD_FLD: "000000001", PRIVATE_NAME_FLD: "משה", FAMILY_NAME_FLD: "כהן", EMPLOYEE_ORGANIZATION_FLD: 0}
        )
        self._collection.insert_one(
            {EMPLOYEE_ID_FLD: self._get_id(), IDENTITY_CARD_FLD: "000000002", PRIVATE_NAME_FLD: "חיים", FAMILY_NAME_FLD: "לוי", EMPLOYEE_ORGANIZATION_FLD: 0}
        )
        self._collection.insert_one(
            {EMPLOYEE_ID_FLD: self._get_id(), IDENTITY_CARD_FLD: "000000003", PRIVATE_NAME_FLD: "אליהו", FAMILY_NAME_FLD: "אדלר",EMPLOYEE_ORGANIZATION_FLD: 0}
        )
        self._collection.insert_one(
            {EMPLOYEE_ID_FLD: self._get_id(), IDENTITY_CARD_FLD: "000000004", PRIVATE_NAME_FLD: "בנימין", FAMILY_NAME_FLD: "טמיר", EMPLOYEE_ORGANIZATION_FLD: 0}
        )
        self._collection.insert_one(
            {EMPLOYEE_ID_FLD: self._get_id(), IDENTITY_CARD_FLD: "000000005", PRIVATE_NAME_FLD: "גיל", FAMILY_NAME_FLD: "כהן", EMPLOYEE_ORGANIZATION_FLD: 0}
        )
        self._collection.insert_one(
            {EMPLOYEE_ID_FLD: self._get_id(), IDENTITY_CARD_FLD: "000000006", PRIVATE_NAME_FLD: "רחל", FAMILY_NAME_FLD: "דהן", EMPLOYEE_ORGANIZATION_FLD: 1}
        )
        self._collection.insert_one(
            {EMPLOYEE_ID_FLD: self._get_id(), IDENTITY_CARD_FLD: "000000007", PRIVATE_NAME_FLD: "חנה", FAMILY_NAME_FLD: "הלר", EMPLOYEE_ORGANIZATION_FLD: 1}
        )
        self._collection.insert_one(
            {EMPLOYEE_ID_FLD: self._get_id(), IDENTITY_CARD_FLD: "000000008", PRIVATE_NAME_FLD: "דקלה", FAMILY_NAME_FLD: "כהנא", EMPLOYEE_ORGANIZATION_FLD: 1}
        )
        self._collection.insert_one(
            {EMPLOYEE_ID_FLD: self._get_id(), IDENTITY_CARD_FLD: "000000009", PRIVATE_NAME_FLD: "אורית", FAMILY_NAME_FLD: "סגל", EMPLOYEE_ORGANIZATION_FLD: 2}
        )
        self._collection.insert_one(
            {EMPLOYEE_ID_FLD: self._get_id(), IDENTITY_CARD_FLD: "0000000010", PRIVATE_NAME_FLD: "משה", FAMILY_NAME_FLD: "כהן", EMPLOYEE_ORGANIZATION_FLD: 2}
        )
        self._collection.insert_one(
            {EMPLOYEE_ID_FLD: self._get_id(), IDENTITY_CARD_FLD: "0000000011", PRIVATE_NAME_FLD: "יעקב", FAMILY_NAME_FLD: "שפרן", EMPLOYEE_ORGANIZATION_FLD: 3}
        )
        self._collection.insert_one(
            {EMPLOYEE_ID_FLD: self._get_id(), IDENTITY_CARD_FLD: "0000000012", PRIVATE_NAME_FLD: "יהודה", FAMILY_NAME_FLD: "רז", EMPLOYEE_ORGANIZATION_FLD: 3}
        )
        self._collection.insert_one(
            {EMPLOYEE_ID_FLD: self._get_id(), IDENTITY_CARD_FLD: "0000000013", PRIVATE_NAME_FLD: "רויטל", FAMILY_NAME_FLD: "לוי", EMPLOYEE_ORGANIZATION_FLD: 3}
        )
        self._collection.insert_one(
            {EMPLOYEE_ID_FLD: self._get_id(), IDENTITY_CARD_FLD: "0000000014", PRIVATE_NAME_FLD: "שני", FAMILY_NAME_FLD: "שרעבי", EMPLOYEE_ORGANIZATION_FLD: 3}
        )
        self._collection.insert_one(
            {EMPLOYEE_ID_FLD: self._get_id(), IDENTITY_CARD_FLD: "0000000015", PRIVATE_NAME_FLD: "מרגלית", FAMILY_NAME_FLD: "הלל", EMPLOYEE_ORGANIZATION_FLD: 4}
        )
        self._collection.insert_one(
            {EMPLOYEE_ID_FLD: self._get_id(), IDENTITY_CARD_FLD: "0000000016", PRIVATE_NAME_FLD: "נוי", FAMILY_NAME_FLD: "חביב", EMPLOYEE_ORGANIZATION_FLD: 4}
        )
        self._collection.insert_one(
            {EMPLOYEE_ID_FLD: self._get_id(), IDENTITY_CARD_FLD: "0000000017", PRIVATE_NAME_FLD: "דניאל", FAMILY_NAME_FLD: "צחור", EMPLOYEE_ORGANIZATION_FLD: 4}
        )
        self._collection.insert_one(
            {EMPLOYEE_ID_FLD: self._get_id(), IDENTITY_CARD_FLD: "0000000018", PRIVATE_NAME_FLD: "סהר", FAMILY_NAME_FLD: "סלומון", EMPLOYEE_ORGANIZATION_FLD: 4}
        )

    def get_employees_by_organization(self, organization_id):
        # Selects the employees of the organizations and sorts them by family and private names
        return list(
            self._collection.find(
                {EMPLOYEE_ORGANIZATION_FLD: organization_id}
            ).sort(
                [(FAMILY_NAME_FLD, pymongo.ASCENDING), (PRIVATE_NAME_FLD, pymongo.ASCENDING)]
            )
        )

    @staticmethod
    def get_employee_place(employee):
        # Finds the name of the employee's place
        places = Places()
        employee_place = places.get_place_by_employee(employee[EMPLOYEE_ID_FLD])
        if len(employee_place):
            return {EMPLOYEE_PLACE_ID_FLD: employee_place[0]["id"], EMPLOYEE_PLACE_NAME_FLD: employee_place[0]["name"]}
        else:
            return {EMPLOYEE_PLACE_ID_FLD: -1, EMPLOYEE_PLACE_NAME_FLD: "בית"}
