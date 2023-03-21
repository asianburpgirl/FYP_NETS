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


@app.route('/')
def getDestination():
     with app.app_context():
        import carpark
        return carpark.get_all()
      
def getCoord():
    locationList = getDestination()
    return locationList

# http://127.0.0.1:5009/getCoords
@app.route('/getCoords',  methods = ['POST'])
def getLatLong():
    latitude = ''
    longitude = ''
    destination = getCoord()
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
