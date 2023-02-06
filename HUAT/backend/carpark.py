from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
from os import environ
import random
import string

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/localconnect'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
    'dbURL') or 'mysql+mysqlconnector://root:root@localhost:8889/localconnect'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}


db = SQLAlchemy(app)
CORS(app)


class Carpark(db.Model):
    __tablename__ = 'carParkDetails'

    carparkID = db.Column(db.Integer, primary_key=True)
    carparkName = db.Column(db.String(100), nullable=False)
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
    
    def __init__(self, carparkID, carparkName, maxCapacity, currentCapacity, hourlyweekdaypeak, hourlyweekdaynonpeak, hourlyweekendpeak, hourlyweekendnonpeak, seasonweekdaypeak, seasonweekdaynonpeak, seasonweekendpeak, seasonweekendnonpeak):
        self.carparkID = carparkID
        self.carparkName = carparkName
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
            "maxCapacity": self.maxCapacity,
            "currentCapacity": self.currentCapacity,
            "hourlyweekdaypeak": self.hourlyweekdaypeak,
            "hourlyweekdaynonpeak": self.hourlyweekdaynonpeak,
            "hourlyweekendpeak": self.hourlyweekendpeak, 
            "hourlyweekendnonpeak": self.hourlyweekendnonpeak,
            "seasonweekdaypeak": self.seasonweekdaypeak, "seasonweekdaynonpeak": self.seasonweekdaynonpeak, "seasonweekendpeak": self.seasonweekendpeak, "seasonweekendnonpeak": self.seasonweekendnonpeak, 
        }

#Get All carparks
@app.route("/carparks")
def get_all():
    carparkList = Carpark.query.all()
    if len(carparkList):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "users": [user.json() for user in carparkList]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no users."
        }
    ), 404


# create user
# @app.route("/users", methods=['POST'])
# def createUser():

#     # bookingID = request.json.get('bookingID' , None)
#     userID = ''.join(random.SystemRandom().choice(string.digits)
#                      for _ in range(6))
#     email = request.json.get('email', None)
#     name = request.json.get('name', None)
#     phoneNum = request.json.get('phoneNum', None)
#     username = request.json.get('username', None)
#     password = request.json.get('password', None)

#     newUser = User(userID=userID, email=email, name=name,
#                    phoneNum=phoneNum, username=username, password=password)

#     try:
#         db.session.add(newUser)
#         db.session.commit()

#     except Exception as e:
#         print(e)
#         return jsonify({
#             "code": 500,
#             "data": {
#                 "userID": userID
#             },
#             "message": "An error occurred collecting the users information"
#         }), 500

#     return jsonify(
#         {
#             "code": 201,
#             "data": newUser.json(),
#             "message": "Your account has been created"
#         }
#     ), 201

# update user password
# @app.route("/users/<int:userID>", methods=["PUT"])
# def updateUser(userID):
#     data = request.get_json()
#     user = User.query.filter_by(userID=userID).first()
#     if user:
#         if data['password']:
#             user.password = data['password']

#             db.session.commit()
#             return jsonify(
#                 {
#                     "code": 200,
#                     "message": "Password update successful!"
#                 }
#             )

#     else:
#         return jsonify(
#             {
#                 "code": 404,
#                 "message": "User cannot be found"
#             }
#         )

# delete user
# @app.route("/users/<int:userID>", methods=['DELETE'])
# def deleteUser(userID):
#     user = User.query.filter_by(userID=userID).first()
#     if user:
#         db.session.delete(user)
#         db.session.commit()
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": {
#                     "userID": userID,

#                 },
#                 "message": "Account has been deleted!"
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "data": {
#                 "userID": userID
#             },
#             "message": "User not found."
#         }
#     ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
