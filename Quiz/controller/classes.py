from db import client
from flask import request, jsonify
from bson import json_util
import json

db = client['Quiz']

collection1 = db['EasyQuestions']

collection2 = db['MediumQuestions']

collection3 = db['Questions']

class Level:
    def __init__(self):
        a = 10

    
    def level(self,response):
        if(response == "EASY"):
            return collection1
        elif(response == "MEDIUM"):
            return collection2
        elif(response == "HARD"):
            return collection3
    
response = input("Choose your choice of level: (EASY, MEDIUM OR HARD)").upper()
coll = Level.level(response)

class Data():
    def getData():
        try:
            data=coll.find({'answer':0})
            arr = []
            for x in data:
                x['_id'] = str(x['_id'])
                arr.append(x) 
            return json.dumps(arr, indent = 4, default= json_util.default)

        except Exception as e:
            print("----ERROR-----",e)
        return{},301
    def addData():
        try:
            data = request.get_json()
            return data
        except Exception as e:
            print("---ERROR-----",e)
        return {},301


class Quiz:
    def check_answers(self,correct_ans,user_ans):
        if(correct_ans == user_ans):

            guess += 1
            return jsonify({"Status" : "-----CORRECT ANSWER-----"})
        else:
            
            return jsonify({"Status" : "----INCORRECT ANSWER-----"})
    def game_begins(self):

        user_answers = []
        question_num = 1
        global guess
        guess=0
        Data.getData()

        user_answer = input("Choose an Option : (A B C or D) or type hint to get one").upper()

        print("----------------")

        guess += self.check_answers(coll.find('answer'),user_answer)
        question_num+=1


   
class Score:
    def score(self,g):
        x = ((g/5)*100)
        return self.x

class Replay:
    def play_again():
        user_response = input("Do you want to play again?: (Yes or No)").upper()
        a = Data.addData()
        if (a == "YES"):
            return 1
        else:
            return 0
    
