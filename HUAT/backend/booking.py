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

    user = db.relationship('User', primaryjoin='Booking.userID == User.userID', backref='booking')


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
    
#get booking by userID
@app.route("/bookings/<int:userID>")
def get_by_user(userID):
    userBooking = Booking.query.filter_by(userID=userID).all()
    if len(userBooking):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "bookings": [booking.json() for booking in userBooking]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no bookings."
        }
    ), 404
    
#get most common 3 bookings by userID
@app.route("/commonCarparks/<int:userID>")
def get_common_carparks(userID):
    todayMonth = date.today().month
    userBooking = Booking.query.filter_by(userID=userID).all()
    
    if len(userBooking):
        common_3_carparks = {}
        for eachBooking in userBooking:
            
            if eachBooking.bookingStartDateTime.month == todayMonth or eachBooking.bookingStartDateTime.month == todayMonth-1 or eachBooking.bookingStartDateTime.month == todayMonth -2 or eachBooking.bookingStartDateTime.month == todayMonth -3:
                if eachBooking.bookingLocation in common_3_carparks:
                    common_3_carparks[eachBooking.bookingLocation] += 1
                else:
                    common_3_carparks[eachBooking.bookingLocation] = 1
        common_3_dict = []
        if len(common_3_carparks) <3 :
            pass
        else: 
            sort_dict = sorted(common_3_carparks.items(), key=lambda x:x[1], reverse= True)
            common_3_dict.append(sort_dict[0][0])
            common_3_dict.append(sort_dict[1][0])
            common_3_dict.append(sort_dict[2][0])
        
        return jsonify(
            {
                "code": 200,
                "data": {
                    "carparks": [carparks for carparks in common_3_dict]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no bookings."
        }
    ), 404
    
#get all carparks booked in common 3 carparks by userID
@app.route("/commonBookingsAll/<int:userID>", methods=['POST'])
def get_common_bookings(userID):
    discount = request.json.get('discount', 0)
    # discount = 0.1
    todayMonth = date.today().month 
    userBooking = Booking.query.filter_by(userID=userID).all()
    
    if len(userBooking):
        common_bookings_all = []
        for eachBooking in userBooking:
            if eachBooking.bookingStartDateTime.month == todayMonth or eachBooking.bookingStartDateTime.month == todayMonth-1 or eachBooking.bookingStartDateTime.month == todayMonth -2 :
                common_bookings_all.append(eachBooking)
        
        total_amt = 0
        for booking in common_bookings_all:
            total_amt += booking.bookingAmt
        discounted_price = (1-discount) * total_amt
        return jsonify(
            {
                "code": 200,
                "data": {
                    "bookings": [bookings.json() for bookings in common_bookings_all],
                    "discountedPrice": round(discounted_price/3,2),
                    "totalPrice": round(total_amt/3,2),
                    "discount": round(total_amt/3 - discounted_price/3,2)
                    
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no bookings."
        }
    ), 404

# Create a new booking
@app.route("/bookings", methods=['POST'])
def createBooking():
    bookingIDList = []
    userBooking = Booking.query.all()
    
    bookingID = 1
    if len(userBooking):
        for eachBooking in userBooking:
            bookingIDList.append(eachBooking.bookingID)
        bookingIDList.sort( reverse=True)
        bookingID = bookingIDList[0] +1 
    
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
 
    print(data)

    if booking:
        if data.get('bookingLocation') != None:
                    booking.bookingLocation = data['bookingLocation']
        if data.get('bookingDateTime') != None:
            booking.bookingDateTime = data['bookingDateTime']
        if data.get('status') != None:
            booking.status = data['status']
        if data.get('bookingStartDateTime') != None:
            booking.bookingStartDateTime = data['bookingStartDateTime']
        if data.get('bookingEndDateTime') != None:
            booking.bookingEndDateTime = data['bookingEndDateTime']
                    
    # if booking:
    #     if data['bookingLocation']:
    #         booking.bookingLocation = data['bookingLocation']
    #     if data['bookingDateTime']:
    #         booking.bookingDateTime = data['bookingDateTime']
    #     if data['status']:
    #         booking.status = data['status']
    #     if data['bookingStartDateTime']:
    #         booking.bookingStartDateTime = data['bookingStartDateTime']
    #     if data['bookingEndDateTime']:
    #         booking.bookingEndDateTime = data['bookingEndDateTime']
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

# credit and refund payment
@app.route("/updateBalance/<int:bookingID>", methods=['PUT'])
def updateBalance(bookingID):
    data = request.get_json()
    booking = Booking.query.filter_by(bookingID=bookingID).first()
    userInfo = User.getUserId(booking.json()['userID'])
    user = User.query.filter_by(userID=userInfo['userID']).first()
    balance = user.json()['balance']

    if booking and user:
        if data['bookingID'] and booking.json()['status'] == 'Booked':
            balance = balance - booking.json()['bookingAmt']
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
            
        #once status == cancel, will trigger the refund (to change status to cancel, refer to updateBooking function)
        if data['bookingID'] and booking.json()['status'] == 'Cancelled':
            balance = balance + booking.json()['bookingAmt']
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
                "bookingID": bookingID
            },
            "message": "Booking ID not found"
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
