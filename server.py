from flask import Flask, jsonify, request
from tinydb import TinyDB, Query
from pprint import pprint

db = TinyDB('db.json')
users = db.table('users') #this is users table
restaurants = db.table('restaurants')
dishes = db.table('dishes')

app = Flask(__name__)

'''
DB functions

'''
# users functionality
def addUser(uname, pwd, email):
    users.insert({'username' : uname, 'password' : pwd, "email" : email})

def returnAllUsers():
    return users.all()

# dishes functionality
def addDish(dish_name, dish_price, dish_pic, dish_ingredients):
    dishes.insert({'dish_name': dish_name, 'dish_price': dish_price, 'dish_pic':dish_pic, 'dish_ingredients': dish_ingredients})

def deleteDish(d_name):
    Dish = Query()
    dishes.remove(Dish.dish_name == d_name)

def editDish(d_name, d_price, d_ingredients):
    Dish = Query()
    dishes.update({'dish_price': d_price, 'dish_ingredients': d_ingredients}, Dish.dish_name == d_name)

def returnAllDishes():
    return dishes.all()

# restaurants functionality
def makeRestaurant(uname):
    restaurants.insert({'username': uname})

def editRestaurant(uname, owner_name, loc, cuisine_types, restaurant_img, r_name):
    # menu or dishes as parameter as well
    Restaurant_User = Query()
    restaurants.update({'owner_name': owner_name, 'location': loc, 'cuisine_types': cuisine_types, 'restaurant_image': restaurant_img, 'restaurant_name': r_name}, Restaurant_User.username == uname)

def returnAllRestaurants():
    return restaurants.all()

'''
Actual Endpoints
'''

@app.route('/home', methods=['GET'])
def jay():
    return jsonify([{"dish_name" : "aloo", "price": 12}, {"dish_name" : "tikki", "price": 20}, {"dish_name" : "dahai", "price": 15}])

@app.route('/api/findChefs', methods=['POST'])
def findChefs():
    body = request.get_json()

    return ""

@app.route('/api/retrieveDishes', methods=['GET'])
def retrieveDishes():
    return ""

@app.route('/api/addDish', methods=['POST']) #TODO
def route_addDish():
    body = request.get_json()
    d_name = body['dish_name']
    d_price = body['dish_price']
    d_pic = body['dish_pic']
    d_ingredients = body['dish_ingredients']

    addDish(d_name, d_price, d_pic, d_ingredients)
    return "Successfully added dish"

@app.route('/api/editDish', methods=['POST']) #TODO
def route_editDish():
    body = request.get_json()
    d_name = body['dish_name']
    d_price = body['dish_price']
    d_ingredients = body['dish_ingredients']

    editDish(d_name, d_price, d_ingredients)
    return "Successfully edited dish"

@app.route('/api/deleteDish', methods=['POST']) #TODO
def route_deleteDish():
    body = request.get_json()
    d_name = body['dish_name']

    deleteDish(d_name)
    return "Successfully deleted dish"

@app.route('/api/signIn', methods=['POST'])
def signIn():
    return ""

@app.route('/api/fetchRestoProfile', methods=['POST'])
def fetchRestoProfile():
    return ""

@app.route('/api/addUser', methods=['POST'])
def route_addUser():
    body = request.get_json() #the request object here is the request that this endpoint recieves (something that someone sent to this)
    uname = body['username']
    pwd = body['password']
    email = body['email']
    addUser(uname, pwd, email)
    makeRestaurant(uname)
    return "Successfully added user"

'''
Test Endpoints
'''

@app.route('/test/returnAllUsers', methods=['GET'])
def test_returnAllUsers():
    return jsonify({'result' : returnAllUsers()})

@app.route('/test/returnAllDishes', methods=['GET'])
def test_returnAllDishes():
    return jsonify({'result': returnAllDishes()})

@app.route('/test/returnAllRestaurants', methods=['GET'])
def test_returnAllRestaurants():
    return jsonify({'result': returnAllRestaurants()})


if __name__ == "__main__":
    app.run(debug=True)

