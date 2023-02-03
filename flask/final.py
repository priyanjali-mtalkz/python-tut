from bson import json_util
import json
from flask import Flask, jsonify, request
import pymongo

app = Flask(__name__)


client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['Subject']
coll = db['Details']

@app.route('/addData',methods = ['POST'])
def addData():
    try:
        data = request.get_json()
        coll.insert_one(data)
        return jsonify({"Status" : "Inserted Successfully"}), 200
    except Exception as e:
        print("---ERROR-----",e)
    return {},301

@app.route('/getData',methods = ['GET'])
def getData():
    try:
        data=coll.find()
        arr = []
        for x in data:
            x['_id'] = str(x['_id'])
            arr.append(x) 

        return json.dumps(arr, indent = 4, default= json_util.default)

    except Exception as e:
        print("----ERROR-----",e)
    return{},301

@app.route('/updateData/<string:name>',methods = ['PUT'])
def updateData(name):
    try:
        data = request.get_json()
        query = {'Name' : name}
        value = {'$set': {'Year' : data['Year']}}
        coll.update_one(query,value)
        return jsonify({"Status" : "Update Successful"}),200
        
    except Exception as e:
        print("-----ERROR-----",e)
    return {},301

@app.route('/deleteData/<string:name>',methods = ['DELETE'])
def deleteData(name):
    try:
        coll.delete_one({'Name' : name})
        return jsonify({"Status" : "Delete Successful"}),200
    except Exception as e:
        print("-----ERROR------",e)
    return {},301


if __name__ == '__main__':
    app.run(debug=True, port = 8888)