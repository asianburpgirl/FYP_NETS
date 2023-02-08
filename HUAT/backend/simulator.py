
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import json
from datetime import datetime
import random
import string

from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
import user
from subprocess import Popen, PIPE, STDOUT
import requests
import os
import ssl

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/localconnect'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root:root@localhost:8889/localconnect'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}


db = SQLAlchemy(app)
CORS(app)


#request type 1000
@app.route("/res/<int:carparkid>", methods=["POST","GET"])
def results(carparkid):
    print("hi")
    payload = {
    "requesttype": 1000,
    "carparkid": carparkid
    }
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post('https://127.0.0.1:9000', json.dumps(payload), headers=headers, verify=False)
    print (r.json())
    # p = Popen(['java', '-jar', 'HUAT/backend/smuxserver.jar','127.0.0.1','8989'],stdout=subprocess.PIPE, stderr=STDOUT)
    # for line in p.stdout.read():
    #     print(line)
    return jsonify (
                {
                    "code": 201,
                    "data": r.json(),
                    "message": "Update successful!"
                }
            ), 201

    
    
    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
