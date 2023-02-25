from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import json
# import json
from os import environ
# import random
# import string

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/localconnect'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root:root@localhost:8889/localconnect'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}


db = SQLAlchemy(app)
CORS(app)


class Carpark(db.Model):
    __tablename__ = 'carparkdetails'

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

    def __init__(self, carparkID, carparkName, carparkLocation, latitude, longitude,imagePath, maxCapacity, currentCapacity, hourlyweekdaypeak, hourlyweekdaynonpeak, hourlyweekendpeak, hourlyweekendnonpeak, seasonweekdaypeak, seasonweekdaynonpeak, seasonweekendpeak, seasonweekendnonpeak):
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
        }

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
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
