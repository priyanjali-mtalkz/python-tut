from flask import Flask, jsonify, request
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
print("Connection Successful")

db = client['Quiz']
collection = db['collection']

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def get_data():
    if(request.method == 'GET'):
        return jsonify(collection.find())

if __name__ == ('__main__'):
    app.run(debug = True)
