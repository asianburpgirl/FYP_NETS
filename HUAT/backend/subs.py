from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
from datetime import datetime
import random
import string
import user
import json
from datetime import date

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/localconnect'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root:root@localhost:8889/localconnect'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)

class Subscription(db.Model):
    __tablename__ = 'subscriptions'

    subsID = db.Column(db.Integer, primary_key=True)
    # subsDateTime = db.Column(db.DateTime, nullable=True)
    # not using the date time now, i put here just in case
    subsDateTime = db.Column(db.Integer,  nullable=False)
    subsTypeID = db.Column(db.Integer,  nullable=False)
    status = db.Column(db.String(128), nullable=False)
    subsRef = db.Column(db.String(128), nullable=False)
    subsAmt = db.Column(db.Float, nullable=False)
    userID = db.Column(db.ForeignKey('users.userID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    user = db.relationship('User', primaryjoin='Subscription.userID == User.userID', backref='subscriptions')


    def __init__(self, subsID, subsDateTime, subsTypeID ,status, subsRef, subsAmt, userID):
        self.subsID = subsID
        self.subsDateTime = subsDateTime
        self.subsTypeID = subsTypeID
        self.status = status
        self.subsRef = subsRef
        self.userID = userID
        self.subsAmt = subsAmt

    def json(self):
        return {
            "subsID": self.subsID,
            "subsDateTime": self.subsDateTime,
            "subsTypeID": self.subsTypeID,
            "status": self.status,
            "subsRef": self.subsRef,
            "userID": self.userID,
            "subsAmt": self.subsAmt,
        }

class User(db.Model):
    __tablename__ = 'users'

    userID = db.Column(db.Integer, primary_key = True)
    email = db.Column (db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phoneNum = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    balance = db.Column(db.Float())
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

    def getUserId(userID):
        user = User.query.filter_by(userID=userID).first()
        return user.json()


# Get All Subscriptions
@app.route("/subs")
def get_all():
    subsList = Subscription.query.all()
    if len(subsList):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "subscriptions": [subscription.json() for subscription in subsList]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no subscriptions."
        }
    ), 404
    
#get subscription by userID
@app.route("/subs/<int:userID>")
def get_by_user(userID):
    userSubs = Subscription.query.filter_by(userID=userID).all()
    if len(userSubs):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "subscriptions": [subscription.json() for subscription in userSubs]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no subscriptions."
        }
    ), 404
    
#check if user already has subscription
@app.route("/subs/<int:userID>&<int:subsID>")
def check_if_subs_exists(userID,subsID):
    userSubs = Subscription.query.filter_by(userID=userID).all()
    if len(userSubs):
        subsExists = False
        subsByType = Subscription.query.filter_by(subsTypeID=subsID).all()
        if len(subsByType):
            subsExists = True
            
        return jsonify(
            {
                "code": 200,
                "data": {
                    "subscriptionsExists": subsExists,
                    
                }
            }
        )
            
        
    return jsonify(
        {
            "code": 404,
            "message": "There are no subscriptions."
        }
    ),404
    
# Create a new subscription
@app.route("/subs", methods=['POST'])
def createSubscription():
    subsIDList = []
    userSubs = Subscription.query.all()
    
    subsID = 1
    if len(userSubs):
        for eachSubs in userSubs:
            subsIDList.append(eachSubs.subsID)
        subsIDList.sort( reverse=True)
        subsID = subsIDList[0] +1 
    
    subsRef = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits)
                        for _ in range(10))
    subsDateTime = request.json.get('subsDateTime', None)
    subsTypeID = request.json.get('subsTypeID', None)
    subsAmt = request.json.get('subsAmt', None)
    status = request.json.get('status', None)
    userID = request.json.get('userID', None)

    newSubs = Subscription(
        subsID=subsID, subsDateTime=subsDateTime,status=status, userID=userID, subsRef=subsRef, subsAmt=subsAmt, subsTypeID= subsTypeID)

    try:
        db.session.add(newSubs)
        db.session.commit()

    except Exception as e:
        print(e)
        return jsonify({
            "code": 500,
            "data": {
                "subsID": subsID
            },
            "message": "An error occurred collecting"
        }), 500

    return jsonify(
        {
            "code": 201,
            "data": newSubs.json(),
            "message": "Ssubscription has been created"
        }
    ), 201

# credit and refund payment
@app.route("/updateBalanceSub/<int:subsID>", methods=['PUT'])
def updateBalance(subsID):
    data = request.get_json()
    subscription = Subscription.query.filter_by(subsID=subsID).first()
    userInfo = User.getUserId(subscription.json()['userID'])
    user = User.query.filter_by(userID=userInfo['userID']).first()
    balance = user.json()['balance']

    if subscription and user:
        if data['subsID'] and subscription.json()['status'] == 'Subscribed':
            balance = balance - subscription.json()['subsAmt']
            user.balance = balance
            print(balance)
            db.session.commit()
            return jsonify(
                {
                    "code": 201,
                    "data": balance,
                    "message": "Update successful!"
                }
            ), 201
            
        #once status == cancel, will trigger the refund (to change status to cancel, refer to updateSubscription function)
        if data['subsID'] and subscription.json()['status'] == 'Cancelled':
            balance = balance + subscription.json()['subsAmt']
            # balance = user.json()['balance']
            user.balance = balance
            print(balance)
            db.session.commit()
            return jsonify(
                {
                    "code": 201,
                    "data": balance,
                    "message": "Update successful!"
                }
            ), 201
            

    else:
        return jsonify({
            "code": 500,
            "data": {
                "subsID": subsID
            },
            "message": "Subscription ID not found"
        }), 500


# update subscription
@app.route("/subs/<int:subsID>", methods=['PUT'])
def updateSubscription(subsID):
    data = request.get_json()
    subs = Subscription.query.filter_by(subsID=subsID).first()
 
    print(data)

    if subs:
        if data.get('status') != None:
            subs.status = data['status']
        
        db.session.commit()
        return jsonify(
            {
                "code": 201,
                "message": "Update successful!"
            }
        ), 201

    else:
        return jsonify({
            "code": 500,
            "data": {
                "subsID": subsID
            },
            "message": "Subscription ID not found"
        }), 500

# delete subscriptions
@app.route("/subs/<int:subsID>", methods=['DELETE'])
def deleteSubscription(subsID):
    subs = Subscription.query.filter_by(subsID=subsID).first()
    if subs:
        db.session.delete(subs)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "subsID": subsID,
                },
                "message": "Subscription successfully deleted!"
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "subsID": subsID,
            },
            "message": "Subscription not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
