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
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/localconnect'
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root:root@localhost:8889/localconnect'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}


db = SQLAlchemy(app)
CORS(app)


class Booking(db.Model):
    __tablename__ = 'bookings'

    bookingID = db.Column(db.Integer, primary_key=True)
    bookingDate = db.Column(db.DateTime, nullable=False)
    bookingLocation = db.Column(db.String(128), nullable=False)
    locationName = db.Column(db.String(128), nullable=False)
    startTime = db.Column(db.DateTime, nullable=False)
    endTime = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(128), nullable=False)
    bookingRef = db.Column(db.String(128), nullable=False)
    # image = db.Column(db.Blob, nullable=True)
    # maxCapacity = db.Column(db.Integer, nullable=False)
    # currentCapacity = db.Column(db.Integer, nullable=False)
    userID = db.Column(db.ForeignKey('users.userID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    user = db.relationship('User', primaryjoin='Booking.userID == User.userID', backref='booking')

    def __init__(self, bookingID, bookingDate,  bookingLocation, locationName, startTime, endTime, status, userID, bookingRef):
        self.bookingID = bookingID
        self.bookingDate = bookingDate
        self.bookingLocation = bookingLocation
        self.locationName = locationName
        self.startTime = startTime
        self.endTime = endTime
        self.status = status
        self.bookingRef = bookingRef
        # self.image = image
        # self.maxCapacity = maxCapacity
        # self.currentCapacity = currentCapacity
        self.userID = userID

    def json(self):
        return {
            "bookingID": self.bookingID,
            "bookingDate": self.bookingDate,
            "bookingLocation": self.bookingLocation,
            "locationName": self.locationName,
            "startTime": self.startTime,
            "endTime": self.endTime,
            "status": self.status,
            "bookingRef": self.bookingRef,
            # "image": self.image,
            # "maxCapacity": self.maxCapacity,
            # "currentCapacity": self.currentCapacity,
            # "image": self.image,
            "userID": self.userID
        }

class User(db.Model):
    __tablename__ = 'users'

    userID = db.Column(db.Integer, primary_key = True)
    email = db.Column (db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phoneNum = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    

    def __init__(self, userID, email, name, phoneNum, username, password):
        self.userID = userID
        self.email = email
        self.name = name
        self.phoneNum = phoneNum
        self.username = username
        self.password = password

    def json(self):
        return {
            "userID": self.userID,
            "email": self.email,
            "name": self.name,
            "phoneNum": self.phoneNum,
            "username": self.username,
            "password": self.password
        }


# Get All Bookings
@app.route("/bookings")
def get_all():
    bookingList = Booking.query.all()
    if len(bookingList):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "bookings": [booking.json() for booking in bookingList]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no applications."
        }
    ), 404


@app.route("/bookings", methods=['POST'])
def createBooking():

    bookingID = ''.join(random.SystemRandom().choice(string.digits) for _ in range(6))
    bookingRef = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits)
                        for _ in range(10))
    bookingDate = request.json.get('bookingDate', None)
    bookingLocation = request.json.get('bookingLocation', None)
    locationName = request.json.get('locationName', None)
    startTime = request.json.get('startTime', None)
    endTime = request.json.get('endTime', None)
    status = request.json.get('status', None)
    # maxCapacity = request.json.get('maxCapacity', None)
    # currentCapacity = request.json.get('currentCapacity', None)
    userID = request.json.get('userID', None)

    newBooking = Booking(
        bookingID=bookingID, bookingDate=bookingDate, bookingLocation=bookingLocation, locationName=locationName, startTime=startTime, endTime=endTime, status=status, userID=userID, bookingRef=bookingRef)

    try:
        db.session.add(newBooking)
        db.session.commit()

    except Exception as e:
        print(e)
        return jsonify({
            "code": 500,
            "data": {
                "bookingID": bookingID
            },
            "message": "An error occurred collecting"
        }), 500

    return jsonify(
        {
            "code": 201,
            "data": newBooking.json(),
            "message": "Your booking has been created"
        }
    ), 201


# update bookings
@app.route("/bookings/<int:bookingID>", methods=['PUT'])
def updateBooking(bookingID):
    data = request.get_json()
    booking = Booking.query.filter_by(bookingID=bookingID).first()
    print(data['bookingDate'])
    print(data)
    if booking:
        if data['bookingLocation']:
            print(data['bookingLocation'])
            booking.bookingLocation = data['bookingLocation']
            db.session.commit()
            return jsonify(
                {
                    "code": 201,
                    "message": "Update successful!"
                }
            ), 201

        if data['bookingDate']:
            print(data['bookingDate'])
            booking.bookingDate = data['bookingDate']
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
                "bookingID": bookingID
            },
            "message": "Booking ID not found"
        }), 500

# delete bookings
@app.route("/bookings/<int:bookingID>", methods=['DELETE'])
def deleteBooking(bookingID):
    booking = Booking.query.filter_by(bookingID=bookingID).first()
    if booking:
        db.session.delete(booking)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "bookingID": bookingID,

                },
                "message": "Booking successfully deleted!"
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "BookingID": bookingID,
            },
            "message": "Booking not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
