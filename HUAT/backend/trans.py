from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
from datetime import datetime
import random
import string
import user
import json

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/localconnect'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root:root@localhost:8889/localconnect'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)


class Transaction(db.Model):
    __tablename__ = 'transaction'

    transID = db.Column(db.Integer, primary_key=True)
    transDate = db.Column(db.DateTime, nullable=False)
    transType = db.Column(db.String(128), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    userID = db.Column(db.ForeignKey('users.userID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    user = db.relationship('User', primaryjoin='Transaction.userID == User.userID', backref='transaction')


    def __init__(self, transID,  transDate, transType, amount):
        self.transID = transID
        self.transDate = transDate
        self.transType = transType
        self.amount = amount


    def json(self):
        return {
            "transID": self.transID,
            "transDate": self.transDate,
            "transType": self.transType,
            "amount": self.amount,
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
    

@app.route("/transaction/<int:userID>")
def get_by_user(userID):
    userBooking = Transaction.query.filter_by(userID=userID).all()
    if len(userBooking):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "bookings": [transaction.json() for transaction in userBooking]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no bookings."
        }
    ), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, debug=True)