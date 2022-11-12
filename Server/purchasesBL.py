from purchasesDBDal import *
from pymongo import MongoClient
from bson import ObjectId


class PurchaseBL:
    def __init__(self):
        self.__purchasesDBDal = PurchasesDBDal()

    def get_purchases_data(self):
        purchases = []
        resp = self.__purchasesDBDal.get_all_purchases()
        if resp == None:
            return "There is no purchases in our system"
        for purchase in resp:
            obj = {
                "Id": purchase["Id"],
                "CustomerID": purchase["CustomerID"],
                "ProductID": purchase["ProductID"],
                "Date": purchase["Date"]
            }
            purchases.append(obj)
        return purchases

    # get by id

    def get_one_purchase_data(self, id):
        purchase = self.__purchasesDBDal.get_one_purchase_data(id)
        if purchase == None:
            return "There isn't no purchase with these ID"
        else:
            return {
                "Id": purchase["Id"],
                "CustomerID": purchase["CustomerID"],
                "ProductID": purchase["ProductID"],
                "Date": purchase["Date"]
            }
    # add

    def add_purchases(self, obj):
        product_test = self.__purchasesDBDal.product_test(
            obj["ProductID"])
        customer_test = self.__purchasesDBDal.customer_test(
            obj["CustomerID"])
        if product_test == None:
            return {"status": "There is no product with this identity"}
        elif product_test["Quantity"] == 0:
            return {"status": "The product is out of stock"}
        elif customer_test == None:
            return {"status": "There is no customer with this identity"}
        else:
            resp = self.__purchasesDBDal.get_all_purchases()
            id = 0
            if resp != None:
                for pur in resp:
                    if pur["Id"] > id:
                        id = pur["Id"]
            id = id+1
            newobj = {
                "Id": id,
                "CustomerID": obj["CustomerID"],
                "ProductID": obj["ProductID"],
                "Date": obj["Date"]
            }
            self.__purchasesDBDal.add_purchase(newobj)
            quantity = product_test["Quantity"]-1
            obj = {
                "Id": product_test["Id"],
                "Name": product_test["Name"],
                "Price": product_test["Price"],
                "Quantity": quantity
            }
            return {"status": "The purchase was added to the system!",
                    "product_to_update": obj
                    }

    def update_purchase_data(self, id, obj):
        resp = self.__purchasesDBDal.get_one_purchase_data(id)
        if resp == None:
            return "Not found Purchase in client system with this identity"
        else:
            newobj = {
                "CustomerID": obj["CustomerID"],
                "ProductID": obj["ProductID"],
                "Date": obj["Date"]
            }
        self.__purchasesDBDal.update_purchase(id, newobj)
        return "purchase data was updated"

    def delete_purchase_id(self, id):
        purchase = self.__purchasesDBDal.get_one_purchase_data(id)
        if purchase == None:
            return "There isn't no purchase with these ID"
        else:
            self.__purchasesDBDal.delete_purchase_by_id(id)
            return "product data was deleted!"

    def get_all_customers_data_purchased_this_product_by_product_ID(self, id):
        product_test = self.__purchasesDBDal.product_test(id)
        if product_test == None:
            return "There is no product with this identity"
        customers = []
        test = False
        purchases = self.__purchasesDBDal.get_all_purchased_for_this_product_by_product_ID(
            id)
        for pur in purchases:
            for cust_id in customers:
                if cust_id["Id"] == pur["CustomerID"]:
                    test = True
            if test == False:
                customer = self.__purchasesDBDal.get_one_customer_data_by_id(
                    pur["CustomerID"])
                obj = {
                    "Id": customer["Id"],
                    "FirstName": customer["FirstName"],
                    "LastName": customer["LastName"],
                    "City": customer["City"],
                    "Date": pur["Date"]
                }
                customers.append(obj)
            else:
                test = False
        if len(customers) == 0:
            return "No customer bought this product"
        else:
            return customers

    def get_all_products_data_purchased_this_customer_by_customer_ID(self, id):
        customer_test = self.__purchasesDBDal.customer_test(id)
        if customer_test == None:
            return "There is no customer with this identity"
        products = []
        test = False
        purchases = self.__purchasesDBDal.get_all_purchased_for_this_customer_by_customer_ID(
            id)
        for pur in purchases:
            for pro_id in products:
                if pro_id["Id"] == pur["CustomerID"]:
                    test = True
            if test == False:
                product = self.__purchasesDBDal.get_one_Product_data_by_id(
                    pur["ProductID"])
                obj = {
                    "Id": product["Id"],
                    "Name": product["Name"],
                    "Price": product["Price"],
                    "Quantity": product["Quantity"],
                    "Date": pur["Date"]
                }
                products.append(obj)
            else:
                test = False
        if len(products) == 0:
            return "The customer did not purchase any product"
        else:
            return products

    def delete_purchase_product_id(self, id):
        product_test = self.__purchasesDBDal.product_test(id)
        if product_test == None:
            return "There is no product with this identify"
        else:
            purchases = self.__purchasesDBDal.get_all_purchased_for_this_product_by_product_ID(
                id)
            for purchase in purchases:
                self.__purchasesDBDal.delete_purchase_by_id(purchase["Id"])
            return "All Purchases Has product id sent was deleted"

    def delete_purchase_customer_id(self, id):
        customer_test = self.__purchasesDBDal.customer_test(id)
        if customer_test == None:
            return "There is no customer with this identity"
        else:
            purchases = self.__purchasesDBDal.get_all_purchased_for_this_customer_by_customer_ID(
                id)
            for purchase in purchases:
                self.__purchasesDBDal.delete_purchase_by_id(purchase["Id"])
            return "All Purchases Has customer id sent was deleted"

    def get_one_purchase_search_obj(self, search_obj):
        customer_test = self.__purchasesDBDal.customer_test(
            search_obj["CustomerID"])
        product_test = self.__purchasesDBDal.product_test(
            search_obj["ProductID"])
        date_test = self.__purchasesDBDal.date_test(search_obj["Date"])
        if customer_test == None:
            return "There is no customer with this identity"
        elif product_test == None:
            return "There is no product with this identity"
        elif date_test == None:
            return "There were no sales that day"
        else:
            purchased = self.__purchasesDBDal.get_purchase_by_proid_cusid_dateid(
                search_obj)
            if purchased == None:
                return "There is no purchase with this data"
            else:
                return {
                    "Id": purchased["Id"],
                    "CustomerID": purchased["CustomerID"],
                    "ProductID": purchased["ProductID"],
                    "Date": purchased["Date"]
                }
