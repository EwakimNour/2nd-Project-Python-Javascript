from pymongo import MongoClient
from bson import ObjectId


class ProductsDBDal:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["projectDB"]

    def get_all_products(self):
        return self.__db["products"].find({})

    # get by id

    def get_one_product_data(self, id):
        return self.__db["products"].find_one(
            {'Id': int(id)})

    def add_product(self, obj):
        self.__db["products"].insert_one(obj)

    def update_product(self, id, obj):
        self.__db["products"].update_one({'Id': int(id)}, {"$set": obj})

    def delete_product(self, id):
        self.__db["products"].delete_one({'Id': int(id)})
