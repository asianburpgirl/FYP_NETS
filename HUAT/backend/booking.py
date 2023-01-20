from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# from itsdangerous import json
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

@app.route("/bookings/<int:bookingID>" , methods = ['POST'])
def createBooking(bookingID):

    # bookingID = request.json.get('bookingID' , None)
    bookingDate = request.json.get('bookingDate' , None)
    bookingLocation = request.json.get('bookingLocation' , None)

    newBooking = Booking(bookingID = bookingID, bookingDate = bookingDate , bookingLocation = bookingLocation)
    
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
