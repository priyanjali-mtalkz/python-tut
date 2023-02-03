from bson import json_util
import json
from flask import Flask, jsonify, request

from class1 import Subject
import pymongo


app = Flask(__name__)


@app.route('/dataSend',methods=['GET','POST'])
def home():
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['Subject']
        coll = db['Details']
        if request.method == 'POST':
            data = request.get_json()
            coll.insert_one(data)
            client.close()
            return jsonify({"status":"Connection Succesfull"}) , 200
        else:
            for ques in coll.find():
                return json.dumps(ques, indent = 4, default = json_util.default)
        

    except Exception as e:
        print("error ::::::::",e)
    return {}, 200


if __name__ == ('__main__'):
    app.run(debug=True, port=9001)




