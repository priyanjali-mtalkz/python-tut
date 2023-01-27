import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
print("Connection Successful")

db = client['Student']
collection = db['Student_details']
n = int(input("Enter the no. of students: "))
arr = []
mydata = {}
for i in range(n):
    
    data1 = "Name"
    name = input("Enter your name: ")
    mydata[data1] = name
    

    data2 = "Age"
    age = input("Enter your age: ")
    mydata[data2] = age

    data3 = "Profile"
    profile = input("Enter your profile: ")
    mydata[data3] = profile

    data4 = "Area"
    area = input("Enter your area: ")
    mydata[data4] = area

    arr.append(mydata)
    mydata = {}

x = db.collection.find().toArray()

if(len(x) > 0):
    print("Data already exists")
else:
    collection.insert_many(arr)



# for i in x:
#     print(i['name'])




