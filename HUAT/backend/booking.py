from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from itsdangerous import json
from os import environ

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/localconnect'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root:root@localhost:8889/localconnect'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}


db = SQLAlchemy(app)
CORS(app)


class Booking(db.Model):
    __tablename__ = 'bookings'

    bookingID = db.Column(db.Integer, primary_key = True)
    bookingDate = db.Column (db.DateTime, nullable=False)
    bookingLocation = db.Column(db.String(100), nullable=False)

    def __init__(self, bookingID, bookingDate, bookingLocation):
        self.bookingID = bookingID
        self.bookingDate = bookingDate
        self.bookingLocation = bookingLocation

    def json(self):
        return {
            "bookingID": self.bookingID,
            "bookingDate": self.bookingDate,
            "bookingLocation": self.bookingLocation
        }

#Get All Bookings
@app.route("/bookings")
def get_all():
    bookingList = Booking.query.all()
    if len(bookingList):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "jobs": [booking.json() for booking in bookingList]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no applications."
        }
    ), 404
