import pymongo 
import time
from classes import *

client = pymongo.MongoClient("mongodb://localhost:27017")
print("Connection Successful")

db = client['Quiz']

collection1 = db['EasyQuestions']

collection2 = db['MediumQuestions']

collection3 = db['Questions']

collection4 = db['UserDetails']








