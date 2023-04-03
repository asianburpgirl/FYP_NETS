import requests
from flask import Flask, jsonify, request
import carpark
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

api_key = "AIzaSyAJXGx7T2ypt5Ew5-9SbDTWF9gqloQUJwI"
url ='https://maps.googleapis.com/maps/api/distancematrix/json?'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root:root@localhost:8889/localconnect'
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


@app.route("/")
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

# http://ec2-13-239-5-115.ap-southeast-2.compute.amazonaws.com:5009/getCoords
@app.route('/getCoords',  methods = ['POST'])
def getLatLong():
    latitude = ''
    longitude = ''
    destination = get_all()
    locationList = []
    myString = "" 
    origin = request.json.get('origin',None)
    # origin = "1.3064433533620563,103.83276247871694" 

    # to get lat and long from the data
    for i in json.loads(destination.data): 
        for j in json.loads(destination.data)['data']:
            for k in json.loads(destination.data)['data'][j]:
                latitude = k['latitude']
                longitude = k['longitude']
                locationList.append([longitude,latitude])
            
    # to concat the lat and long tgt
    for i in locationList:
        myString += str(i[1]) + ',' +str(i[0])+'|'

    # to remove the last pipeline
    myString = myString[0:-1]

    print(url + 'origins=' + origin +'&destinations=' + myString + '&departure_time=now&key=AIzaSyAJXGx7T2ypt5Ew5-9SbDTWF9gqloQUJwI')
    # to request to the google map api
    r = requests.get(url + 'origins=' + origin +'&destinations=' + myString + '&departure_time=now&key=AIzaSyAJXGx7T2ypt5Ew5-9SbDTWF9gqloQUJwI')
         
    # to make it in json format
    x = r.json()
    return x


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5009', debug=True)
