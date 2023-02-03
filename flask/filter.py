import pymongo 

client = pymongo.MongoClient("mongodb://localhost:27017")
print("Connection Successful")

db = client['Student']
collection = db['Student_details']
#query = {"Name" : "Priyanjali"}

#query = {"Age" : {"$gt" : 20}}
#query = {"Age" : {"$gt" : 20, "$lt" : 30}}
#query = {"Name" : {"$regex" : "^P"}}
query = {"Name" : {"$regex" : "i$"}}
docs = collection.find(query)

for doc in docs:
    print(doc)