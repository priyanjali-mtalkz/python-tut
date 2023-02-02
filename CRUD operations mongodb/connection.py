import pymongo 

client = pymongo.MongoClient("mongodb://localhost:27017")
print("Connection Successful")

db = client['Student']
collection = db['Student_details']



mydata = [{
    'name' : 'Priyanjali',
    'Project' : 'Admin page',
    'Coworker' : 5,
    'Deadline' : '7 days'
},
{
    'name' : 'Rohan',
    'Project' : 'Website',
    'Coworker' : 6,
    'Deadlline' : '9 days'

},
{
    'name' : 'Sohan',
    'Project' : 'Bot Building',
    'Coworker' : 10,
    'Deadline' : '5 days'
}]
print("Collection created")
#x = collection.insert_many(mydata)

query = {'name' : 'Rohan'}
value = {'$set': {'Project' : 'Webpage'}}
collection.update_one(query,value)

for ele in collection.find():
    print(ele['Name'])
 
#x=collection.delete_many({})  #To delete all the elements in the collection
#print(x.deleted_count,'Documents deleted')


'''print("Collection after delete")
for doc in collection.find():
    print(doc)'''  #Printing after delete




client.close()



