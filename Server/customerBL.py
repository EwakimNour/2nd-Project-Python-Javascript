from customersDBDal import *
from pymongo import MongoClient
from bson import ObjectId


class CustomerBL:
    def __init__(self):
        self.__customersDBDal = CustomersDBDal()

    # get all customers data

    def get_customers_data(self):
        customers = []
        resp = self.__customersDBDal.get_all_customers_data()
        if resp == None:
            return "There is no product in our system"
        for customer in resp:
            obj = {
                "Id": customer["Id"],
                "FirstName": customer["FirstName"],
                "LastName": customer["LastName"],
                "City": customer["City"]
            }
            customers.append(obj)
        return customers
    # get by id

    def get_one_customer_data(self, id):
        customer = self.__customersDBDal.get_one_customer_data_by_id(id)
        if customer == None:
            return "Not found customer in client system with this identity"
        else:
            return {
                "Id": customer["Id"],
                "FirstName": customer["FirstName"],
                "LastName": customer["LastName"],
                "City": customer["City"]
            }
    # add

    def add_customer(self, obj):
        resp = self.__customersDBDal.get_all_customers_data()
        id = 0
        if resp != None:
            for customer in resp:
                if customer["Id"] > id:
                    id = customer["Id"]
        id = id+1
        newobj = {
            "Id": id,
            "FirstName": obj["FirstName"],
            "LastName": obj["LastName"],
            "City": obj["City"]
        }
        self.__customersDBDal.add_customer(newobj)
        return "The Customer was added to the system!"

    # update by id
    def update_customer_data(self, id, obj):
        customer = self.__customersDBDal.get_one_customer_data_by_id(id)
        if customer == None:
            return "Not found customer in client system with this identity"
        else:
            newobj = {
                "FirstName": obj["FirstName"],
                "LastName": obj["LastName"],
                "City": obj["City"]
            }
        self.__customersDBDal.update_customer(id, newobj)
        return "customer data was updated"
    # delete by id

    def delete_customer(self, id):
        customer = self.__customersDBDal.get_one_customer_data_by_id(id)
        if customer == None:
            return "Not found customer in client system with this identity"
        else:
            self.__customersDBDal.delete_customer(id)
            return "product data was deleted!"
