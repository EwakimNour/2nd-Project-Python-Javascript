from asyncio.windows_events import NULL
import string
from pymongo import MongoClient
from bson import ObjectId


class PurchasesDBDal:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["projectDB"]

    def get_all_purchases(self):
        return self.__db["purchases"].find({})

    def get_one_purchase_data(self, id):
        return self.__db["purchases"].find_one({'Id': int(id)})

    def add_purchase(self, obj):
        self.__db["purchases"].insert_one(obj)

    def update_purchase(self, id, obj):
        self.__db["purchases"].update_one({'Id': int(id)}, {"$set": obj})

    def delete_purchase_by_id(self, id):
        self.__db["purchases"].delete_one({'Id': int(id)})

    def product_test(self, id):
        return self.__db["products"].find_one({'Id': int(id)})

    def customer_test(self, id):
        return self.__db["customers"].find_one({'Id': int(id)})

    def get_all_purchased_for_this_product_by_product_ID(self, id):
        return self.__db["purchases"].find({'ProductID': int(id)})

    def get_all_purchased_for_this_customer_by_customer_ID(self, id):
        return self.__db["purchases"].find({'CustomerID': int(id)})

    def get_one_customer_data_by_id(self, id):
        return self.__db["customers"].find_one({'Id': int(id)})

    def get_one_Product_data_by_id(self, id):
        return self.__db["products"].find_one({'Id': int(id)})

    def date_test(self, id):
        return self.__db["purchases"].find_one({'Date': str(id)})

    def get_purchase_by_proid_cusid_dateid(self, search_obj):
        return self.__db["purchases"].find_one({'ProductID': int(search_obj["ProductID"]), 'CustomerID': int(search_obj["CustomerID"]), 'Date': str(search_obj["Date"])})
