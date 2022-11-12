from flask import Flask, jsonify, request
import json
from bson import ObjectId
from flask_cors import CORS

from customerBL import *
from productsBL import *
from purchasesBL import *
app = Flask(__name__)
CORS(app)


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super(MyEncoder, self).default(obj)


app.json_encoder = MyEncoder

customer_bl = CustomerBL()
product_bl = ProductsBL()
purchase_bl = PurchaseBL()
# customers Router
# Get all


@app.route('/customers', methods=['GET'])
def get_all_customers():
    res = customer_bl.get_customers_data()
    print(res)
    return jsonify(res)


# get by id
@app.route('/customers/<string:id>', methods=['GET'])
def get_customer(id):
    res = customer_bl.get_one_customer_data(id)
    print(res)
    return jsonify(res)


# add customer


@app.route('/customers', methods=['POST'])
def add_customer():
    status = customer_bl.add_customer(request.json)
    return jsonify(status)


# update customer

@app.route('/customers/<string:id>', methods=['PUT'])
def update_customer(id):
    res = customer_bl.update_customer_data(id, request.json)
    return jsonify(res)


# delete customer
@app.route('/customers/<string:id>', methods=['DELETE'])
def delete_customer(id):
    res = customer_bl.delete_customer(id)
    return jsonify(res)

# products Router
# Get all products


@app.route('/products', methods=['GET'])
def get_all_products():
    res = product_bl.get_products_data()
    return jsonify(res)


# get one product by id
@app.route('/products/<string:id>', methods=['GET'])
def get_product(id):
    res = product_bl.get_one_product_data(id)
    return jsonify(res)

# add product


@app.route('/products', methods=['POST'])
def add_product():
    res = product_bl.add_product(request.json)
    return jsonify(res)


# update product

@app.route('/products/<string:id>', methods=['PUT'])
def update_product(id):
    res = product_bl.update_product_data(id, request.json)
    return jsonify(res)


# delete product
@app.route('/products/<string:id>', methods=['DELETE'])
def delete_product(id):
    status = product_bl.delete_product(id)
    return jsonify(status)

# purchases Router
# Get all products


@app.route('/purchases', methods=['GET'])
def get_all_purchases():
    res = purchase_bl.get_purchases_data()
    return jsonify(res)


# get one purchase by id
@app.route('/purchases/<string:id>', methods=['GET'])
def get_one_purchase(id):
    res = purchase_bl.get_one_purchase_data(id)
    return jsonify(res)

# add purchase


@app.route('/purchases', methods=['POST'])
def add_purchase():
    res = purchase_bl.add_purchases(request.json)
    if res["status"] == "The purchase was added to the system!":
        product_bl.update_product_data(
            res["product_to_update"]["Id"], res["product_to_update"])
    return jsonify(res["status"])

# update purchase


@app.route('/purchases/<string:id>', methods=['PUT'])
def update_purchase(id):
    res = purchase_bl.update_purchase_data(id, request.json)
    return jsonify(res)

# delete purchase


@app.route('/purchases/<string:id>', methods=['DELETE'])
def delete_purchase(id):
    res = purchase_bl.delete_purchase_id(id)
    return jsonify(res)

# get all_customers data that purchased this product by product ID


@app.route('/purchases/searchbyproductid/<string:id>', methods=['GET'])
def get_all_customers_purchase(id):
    res = purchase_bl.get_all_customers_data_purchased_this_product_by_product_ID(
        id)

    return jsonify(res)

# List purchased by the customer


@app.route('/purchases/searchbycustomerid/<string:id>', methods=['GET'])
def get_all_purchased(id):
    res = purchase_bl.get_all_products_data_purchased_this_customer_by_customer_ID(
        id)

    return jsonify(res)


# delete purchase by product id


@app.route('/purchases/deletebyproductid/<string:id>', methods=['DELETE'])
def delete_purchases_product_id(id):
    res = purchase_bl.delete_purchase_product_id(id)
    return jsonify(res)

# delete purchase by customer id


@app.route('/purchases/deletebycustomerid/<string:id>', methods=['DELETE'])
def delete_purchases_customer_id(id):
    res = purchase_bl.delete_purchase_customer_id(id)
    return jsonify(res)

# get one purchase by id


@app.route('/purchases/search_obj', methods=['PUT'])
def get_one_purchase_searchobj():
    res = purchase_bl.get_one_purchase_search_obj(request.json)
    return jsonify(res)


app.run()
