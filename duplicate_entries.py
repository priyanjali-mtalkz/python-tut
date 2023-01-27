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


x = []
x = collection.find()
# for i in x:
#     print(i['name'])

if (x[0] == name):
    print("Data already exists")
else:
    collection.insert_many(arr)


