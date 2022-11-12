from pymongo import MongoClient
from bson import ObjectId


class CustomersDBDal:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["projectDB"]

    def get_all_customers_data(self):
        return self.__db["customers"].find({})

    # get by id

    def get_one_customer_data_by_id(self, id):
        return self.__db["customers"].find_one({'Id': int(id)})

    def add_customer(self, obj):
        self.__db["customers"].insert_one(obj)

    def update_customer(self, id, obj):
        self.__db["customers"].update_one({'Id': int(id)}, {"$set": obj})

    def delete_customer(self, id):
        self.__db["customers"].delete_one({'Id': int(id)})
