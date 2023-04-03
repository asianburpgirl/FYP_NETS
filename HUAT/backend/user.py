from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
from os import environ
import random
import string


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/localconnect'
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root:root@localhost:8889/localconnect'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root:DVpPUEwcXIqGtf5exERy@database-1.chvatocqi8u6.us-east-1.rds.amazonaws.com:8889/localconnect'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}


db = SQLAlchemy(app)
CORS(app)


class User(db.Model):
    __tablename__ = 'users'

    userID = db.Column(db.Integer, primary_key = True)
    email = db.Column (db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phoneNum = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    balance = db.Column(db.Float(), nullable=False)
    role = db.Column(db.String(100))
    

    def __init__(self, userID, email, name, phoneNum, username, password, balance,role):
        self.userID = userID
        self.email = email
        self.name = name
        self.phoneNum = phoneNum
        self.username = username
        self.password = password
        self.balance = balance
        self.role = role

    def json(self):
        return {
            "userID": self.userID,
            "email": self.email,
            "name": self.name,
            "phoneNum": self.phoneNum,
            "username": self.username,
            "password": self.password,
            "balance": self.balance,
            "role": self.role
        }

#Get All Users
@app.route("/users")
def get_all():
    userList = User.query.all()
    if len(userList):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "users": [user.json() for user in userList]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no users."
        }
    ), 404

#authenticate user
@app.route("/userlogin", methods=["POST"])
def login_by_username():
    if request.is_json:
        user_details = request.get_json()
        username = user_details["username"]
        password = user_details["password"]
        user = User.query.filter_by(username=username).first()
        if user:
            if user.password == password:
                return jsonify(
                    {
                        "code": 200,
                        "data": json.loads(
                            json.dumps(user.json())
                        ),
                    }
                )
            else:
                return (
                    jsonify({"code": 403, "message": "Wrong password."}),
                    403,
                ) 
        return jsonify({"code": 404, "message": "Customer not found."}), 404
    else:
        return jsonify({"code": 500, "message": "Input is not JSON."}), 500

# create user
@app.route("/users" , methods = ['POST'])
def createUser():
    userIDList = []
    users = User.query.all()
    
    userID = 1
    if len(users):
        for eachBooking in users:
            userIDList.append(eachBooking.userID)
        userIDList.sort( reverse=True)
        userID = userIDList[0] +1 

    email = request.json.get('email' , None)
    name = request.json.get('name' , None)
    phoneNum = request.json.get('phoneNum' , None)
    username = request.json.get('username' , None)
    password = request.json.get('password' , None)
    balance = request.json.get('balance', 0)  
    # balance = request.json.get('balance', None)
    # if role is given, must be Admin. Else, default is User
    if request.get_json().get("role") != None:
        role = "Admin"
    else: 
        role = "User"

    newUser = User( userID = userID, email = email, name = name , phoneNum = phoneNum, username = username, password = password, balance=balance, role= role)
    
    try:
        db.session.add(newUser)
        db.session.commit()
    
    except Exception as e:
        print(e)
        return jsonify({
            "code": 500,
            "data": {
                "userID": userID
            },
            "message": "An error occurred collecting the users information"
        }), 500

    return jsonify(
        {
            "code": 201,
            "data": newUser.json(),
            "message": "Your account has been created"
        }
    ), 201

# update user password
@app.route("/users/<int:userID>", methods = ["PUT"])
def updateUser(userID):
    data = request.get_json()
    user = User.query.filter_by(userID = userID).first()
    if user:
        if data['password']:
            user.password = data['password']

            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "message": "Password update successful!"
                }
            )

    else:
        return jsonify(
            {
                "code": 404,
                "message": "User cannot be found"
            }
        )

# delete user
@app.route("/users/<int:userID>", methods=['DELETE'])
def deleteUser(userID):
    user = User.query.filter_by(userID=userID).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "userID": userID,
                    
                },
                "message": "Account has been deleted!"
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "userID": userID
            },
            "message": "User not found."
        }
    ), 404
    
# check if user exists
@app.route("/checkUserExist")
def checkUser():
    email = request.args.get('email')
    account = request.args.get('account')
    emailAccountCombined = email+"@"+account
    user = User.query.filter_by(email=emailAccountCombined).first()
    if user:
        return jsonify(
                    {
                        "code": 200,
                        "message": "User exists"
                    }
                )
        
    return jsonify(
        {
            "code": 200,
            "message": "User not found"
        }
    )

# get balance based on user ID
@app.route("/getBalance/<int:userID>")
def getBalance(userID):
    user = User.query.filter_by(userID = userID).first()
    print(user.json())
    if user:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "userID" : userID,
                    "balance": user.json()['balance']
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "No such user in the database."
        }
    ), 404

@app.route("/addTen/<int:userID>/<int:balance>", methods=['PUT'])
def addTen(userID, balance):
    user = User.query.filter_by(userID = userID).first()
    balance = user.json()['balance'] 
    if user:
        balance = balance + 10
        user.balance = balance
        # print(user.json()['balance'] + 10)
        db.session.commit()
        return jsonify(
            {
                "code": 201,
                "data": balance,
                "message": "YES!!!"
            }
        ), 201
        
    return jsonify(
        {
            "code": 404,
            "message": "No such user in the database."
        }
    ), 404

@app.route("/addTwenty/<int:userID>/<int:balance>", methods=['PUT'])
def addTwenty(userID, balance):
    user = User.query.filter_by(userID = userID).first()
    balance = user.json()['balance'] 
    print(balance)
    if user:
        balance = balance + 20
        user.balance = balance
        # print(user.json()['balance'] + 10)
        db.session.commit()
        return jsonify(
            {
                "code": 201,
                "data": balance,
                "message": "YES!!!"
            }
        ), 201
        
    return jsonify(
        {
            "code": 404,
            "message": "No such user in the database."
        }
    ), 404

@app.route("/addThirty/<int:userID>/<int:balance>", methods=['PUT'])
def addThirty(userID, balance):
    user = User.query.filter_by(userID = userID).first()
    balance = user.json()['balance'] 
    if user:
        balance = balance + 30
        user.balance = balance
        # print(user.json()['balance'] + 10)
        db.session.commit()
        return jsonify(
            {
                "code": 201,
                "data": balance,
                "message": "YES!!!"
            }
        ), 201
        
    return jsonify(
        {
            "code": 404,
            "message": "No such user in the database."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port="5002")
