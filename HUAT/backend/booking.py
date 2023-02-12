from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
from datetime import datetime
import random
import string
import user

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/localconnect'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root:root@localhost:8889/localconnect'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}


db = SQLAlchemy(app)
CORS(app)


class Booking(db.Model):
    __tablename__ = 'bookings'

    bookingID = db.Column(db.Integer, primary_key=True)
    bookingDateTime = db.Column(db.DateTime, nullable=False)
    bookingLocation = db.Column(db.String(128), nullable=False)
    locationName = db.Column(db.String(128), nullable=False)
    bookingStartDateTime = db.Column(db.DateTime, nullable=False)
    bookingEndDateTime = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(128), nullable=False)
    bookingRef = db.Column(db.String(128), nullable=False)
    bookingAmt = db.Column(db.Float, nullable=False)
    userID = db.Column(db.ForeignKey('users.userID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    user = db.relationship(
        'User', primaryjoin='Booking.userID == User.userID', backref='booking')


    def __init__(self, bookingID,   bookingLocation, locationName, bookingStartDateTime, 
    bookingEndDateTime, status, userID, bookingRef, bookingAmt, bookingDateTime):
        self.bookingDateTime = bookingDateTime
        self.bookingID = bookingID
        self.bookingLocation = bookingLocation
        self.locationName = locationName
        self.bookingStartDateTime = bookingStartDateTime
        self.bookingEndDateTime = bookingEndDateTime
        self.status = status
        self.bookingRef = bookingRef
        self.userID = userID
        self.bookingAmt = bookingAmt

    def json(self):
        return {
            "bookingID": self.bookingID,
            "bookingLocation": self.bookingLocation,
            "locationName": self.locationName,
            "bookingStartDateTime": self.bookingStartDateTime,
            "bookingEndDateTime": self.bookingEndDateTime,
            "status": self.status,
            "bookingRef": self.bookingRef,
            "userID": self.userID,
            "bookingAmt": self.bookingAmt,
            "bookingDateTime": self.bookingDateTime
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
    bookingDateTime = request.json.get('bookingDateTime', None)
    bookingLocation = request.json.get('bookingLocation', None)
    locationName = request.json.get('locationName', None)
    bookingStartDateTime = request.json.get('bookingStartDateTime', None)
    bookingEndDateTime = request.json.get('bookingEndDateTime', None)
    bookingAmt = request.json.get('bookingAmt', None)
    status = request.json.get('status', None)
    userID = request.json.get('userID', None)

    newBooking = Booking(
        bookingID=bookingID, bookingDateTime=bookingDateTime, bookingLocation=bookingLocation, locationName=locationName, bookingStartDateTime=bookingStartDateTime, bookingEndDateTime=bookingEndDateTime, status=status, userID=userID, bookingRef=bookingRef, bookingAmt=bookingAmt)


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
