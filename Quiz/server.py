from bson import json_util
import json
import pymongo 
from flask import Flask,jsonify,request

client = pymongo.MongoClient("mongodb://localhost:27017")
print("Connection Successful")

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug = True, port = 9001)


