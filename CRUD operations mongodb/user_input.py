import pymongo
client = pymongo.MongoClient("mongodb+srv://priyanjali-mtalkz:Asdfghjkl12345@cluster0.fwdubsu.mongodb.net/test")
print("Connection Successful")

db = client['Student']
collection = db['Student_details']

'''name = input("Enter your name: ")
project = input("Enter your project: ")
age = input("Enter your age: ")
area = input("Enter your area: ")


query = {"Name":(name),"StudentAge":(age),"studentArea":(area),"StudentProject":(project)}

collection.insert_one(query)''' #for taking single input
   #for multiple inputs from user
n = int(input("Enter the no. of students: "))
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

 
collection.insert_one(mydata)
print("New details inserted")
