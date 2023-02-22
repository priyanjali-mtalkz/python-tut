from db import client
from bson import json_util
import json
import classes
import time
from model.schema import user_schema
from flask import request,jsonify


db = client['Quiz']
collection4 = db['UserDetails']

arr = []
class User():
    def __inint__(self):
        a = 10

    def getUsers(self):
        
        
        user_id = {}
        for i in range(users):
            errors = user_schema().validate(request.get_json)
            if errors:
                return errors, 422 #unprocessable entity
            

        startTime = time.time()

        classes.Quiz()

        endTime = time.time()
        timetaken = endTime - startTime

        errors = user_schema().validate(request.get_json)
        if errors:
            return errors, 422 #unprocessable entity

        user_schema.validate(timetaken)

        user_schema.validate(classes.Level())
        user_id = user_schema().load(request.get_json)
        arr.append(user_id)
        user_id = {}

    collection4.insert_many(arr)
    #y=collection4.delete_many({})

    
    while(classes.Replay()):
        classes.Quiz()
    print("----------------")
    print("   Thankyou!!   ")
    print("----------------")


