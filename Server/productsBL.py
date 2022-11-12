from productsDBDal import *
from pymongo import MongoClient
from bson import ObjectId


class ProductsBL:
    def __init__(self):
        self.__productsDBDal = ProductsDBDal()

    # get all products data
    def get_products_data(self):
        products = []
        resp = self.__productsDBDal.get_all_products()
        if resp == None:
            return "There is no product in our system"
        for product in resp:
            obj = {
                "Id": product["Id"],
                "Name": product["Name"],
                "Price": product["Price"],
                "Quantity": product["Quantity"]
            }
            products.append(obj)
        return products

    # get by id

    def get_one_product_data(self, id):
        product = self.__productsDBDal.get_one_product_data(id)
        if product == None:
            return "Not found product in client system with this identity"
        else:
            return {
                "Id": product["Id"],
                "Name": product["Name"],
                "Price": product["Price"],
                "Quantity": product["Quantity"]
            }
    # Add One

    def add_product(self, obj):
        resp = self.__productsDBDal.get_all_products()
        id = 0
        if resp != None:
            for pro in resp:
                if pro["Id"] > id:
                    id = pro["Id"]
        id = id+1
        newobj = {
            "Id": id,
            "Name": obj["Name"],
            "Price": obj["Price"],
            "Quantity": obj["Quantity"]
        }
        self.__productsDBDal.add_product(
            newobj)
        return "The product was added to the system!"

    # update by id
    def update_product_data(self, id, obj):
        product = self.__productsDBDal.get_one_product_data(id)
        if product == None:
            return "Not found product in client system with this identity"
        else:
            prod = {}
            prod["Name"] = obj["Name"]
            prod["Price"] = obj["Price"]
            prod["Quantity"] = obj["Quantity"]
            self.__productsDBDal.update_product(id, prod)
            return "product data was updated"

    def delete_product(self, id):
        product = self.__productsDBDal.get_one_product_data(id)
        if product == None:
            return "Not found product in client system with this identity"
        else:
            self.__productsDBDal.delete_product(id)
            return "product data was deleted!"
