from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import json
# import json
from os import environ
import random
import datetime
# import string

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/localconnect'
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root:root@localhost:8889/localconnect'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}


db = SQLAlchemy(app)
CORS(app)


class Carpark(db.Model):
    __tablename__ = 'carparkDetails'

    carparkID = db.Column(db.Integer, primary_key=True)
    carparkName = db.Column(db.String(100), nullable=False)
    carparkLocation = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    imagePath = db.Column(db.String(100), nullable=False)
    maxCapacity = db.Column(db.Integer, nullable=False)
    currentCapacity = db.Column(db.Integer, nullable=False)
    hourlyweekdaypeak = db.Column(db.Integer, nullable=False)
    hourlyweekdaynonpeak = db.Column(db.Integer, nullable=False)
    hourlyweekendpeak = db.Column(db.Integer, nullable=False)
    hourlyweekendnonpeak = db.Column(db.Integer, nullable=False)
    seasonweekdaypeak = db.Column(db.Integer, nullable=False)
    seasonweekdaynonpeak = db.Column(db.Integer, nullable=False)
    seasonweekendpeak = db.Column(db.Integer, nullable=False)
    seasonweekendnonpeak = db.Column(db.Integer, nullable=False)
    chosen = db.Column(db.Integer, nullable=False)

    def __init__(self, carparkID, carparkName, carparkLocation, latitude, longitude,imagePath, maxCapacity, currentCapacity, hourlyweekdaypeak, hourlyweekdaynonpeak, hourlyweekendpeak, hourlyweekendnonpeak, seasonweekdaypeak, seasonweekdaynonpeak, seasonweekendpeak, seasonweekendnonpeak, chosen):
        self.carparkID = carparkID
        self.carparkName = carparkName
        self.carparkLocation = carparkLocation
        self.latitude = latitude
        self.longitude = longitude
        self.imagePath = imagePath
        self.maxCapacity = maxCapacity
        self.currentCapacity = currentCapacity
        self.hourlyweekdaypeak = hourlyweekdaypeak
        self.hourlyweekdaynonpeak = hourlyweekdaynonpeak
        self.hourlyweekendpeak = hourlyweekendpeak
        self.hourlyweekendnonpeak = hourlyweekendnonpeak
        self.seasonweekdaypeak = seasonweekdaypeak
        self.seasonweekdaynonpeak = seasonweekdaynonpeak
        self.seasonweekendpeak = seasonweekendpeak
        self.seasonweekendnonpeak = seasonweekendnonpeak
        self.chosen = chosen

    def json(self):
        return {
            "carparkID": self.carparkID,
            "carparkName": self.carparkName,
            "caparkLocation": self.carparkLocation,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "imagePath": self.imagePath,
            "maxCapacity": self.maxCapacity,
            "currentCapacity": self.currentCapacity,
            "hourlyweekdaypeak": self.hourlyweekdaypeak,
            "hourlyweekdaynonpeak": self.hourlyweekdaynonpeak,
            "hourlyweekendpeak": self.hourlyweekendpeak,
            "hourlyweekendnonpeak": self.hourlyweekendnonpeak,
            "seasonweekdaypeak": self.seasonweekdaypeak, 
            "seasonweekdaynonpeak": self.seasonweekdaynonpeak, 
            "seasonweekendpeak": self.seasonweekendpeak, 
            "seasonweekendnonpeak": self.seasonweekendnonpeak,
            "chosen": self.chosen,
        }

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
    def getAllBookings():
        bookingList = Booking.query.all()
        return bookingList.json()

# Get All carparks
@app.route("/carparks")
def get_all():
    carparkList = Carpark.query.all()

    if len(carparkList):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "carparks": [carpark.json() for carpark in carparkList]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no carparks."
        }
    ), 404

# add carpark capacity by 1
@app.route("/carparkCapAdd/<int:carparkID>")
def addCarparkCapacity(carparkID):
    carparkID = Carpark.query.filter_by(carparkID=carparkID).first()
    if carparkID:
        carparkID.currentCapacity += 1
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "message": str(carparkID) + " added 1 capacity successful!"
            }
        )
    else:
        return jsonify(
            {
                "code": 404,
                "message": "Carpark cannot be found"
            }
        )

# minus carpark capacity by 1
@app.route("/carparkCapMinus/<int:carparkID>")
def minusCarparkCapacity(carparkID):
    carparkID = Carpark.query.filter_by(carparkID=carparkID).first()
    if carparkID:
        carparkID.currentCapacity -= 1
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "message":  str(carparkID) + " minus 1 capacity successful!"
            }
        )
    else:
        return jsonify(
            {
                "code": 404,
                "message": "Carpark cannot be found"
            }
        )

# get carpark image path
@app.route("/carparkImage",methods= ['POST'])
def getCarparkImage():
    carparkNameInput = request.json.get('carparkName', None)
    carparkName = Carpark.query.filter_by(carparkName=carparkNameInput).first()
    
    if carparkName:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "imagePath": carparkName.json()['imagePath']
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no such carparks."
        }
    ), 404
    
#categorise carparks into 4 tiers
@app.route("/carparkCat")
def categoriseCarparkTiers():
    today = datetime.datetime.today()
    today = today.day
    if today == 1:
        bookings = Booking.query.all()
        carparks = Carpark.query.all()
        
        bookings_dict = {}
        if len(bookings):
        #get all carpark names
            carpark_names = []
            for eachCarpark in carparks:
                carpark_names.append(eachCarpark.carparkName)
            # sort all carparks from most popular to least popular
            for eachBooking in bookings:
                if eachBooking.bookingLocation in carpark_names:
                    carpark_names.remove(eachBooking.bookingLocation)
                if eachBooking.bookingLocation in bookings_dict:
                        bookings_dict[eachBooking.bookingLocation] += 1
                else:
                    bookings_dict[eachBooking.bookingLocation] = 1
            bookings_sorted = dict(sorted(bookings_dict.items(), key=lambda x:x[1], reverse= True))
            bookings_list = []
            for location, count in bookings_sorted.items():
                bookings_list.append({"location": location, "count": count})
            
            # in case there is a carpark without any booking
            for missingCarparks in carpark_names:
                bookings_list.append({"location": missingCarparks, "count": 0})
            
            #splitting into tiers 
            no_of_tier = 4 
            tieredBooking = {}
            carparkInEachGroup = len(bookings_list)//no_of_tier 
            count = 1
            myList= []
            for i in range(0, len(bookings_list)):
                myList.append(bookings_list[i])
                if len(myList) == carparkInEachGroup:
                    tieredBooking[count] = myList
                    count += 1
                    myList= []

            chosenCarpark = []
            for (index,eachTier) in tieredBooking.items():
                chosenCarpark.append(random.choices(eachTier))
            
            for eachCarpark in carparks:
                for eachCarpark2 in chosenCarpark:
                    if eachCarpark.carparkName == eachCarpark2[0]["location"]:
                        eachCarpark.chosen = 1
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "bookings": chosenCarpark,
                    }
                }
            )
    return jsonify(
        {
            "code": 404,
            "message": "There are no applications."
        }
    ), 404
    
# return carparks with chosen == 1. ie chosen for the month
@app.route("/chosenCarparks")
def get_chosen_carparks():
    carparks = Carpark.query.filter_by(chosen=1).all()

    if carparks:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "carparks": [carpark.json() for carpark in carparks]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no such carparks."
        }
    ), 404
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
