from flask import Flask
from flask import jsonify,request
# import sys
# path1 = sys.path.insert(1,'D:\mongo_code\pymongo\Quiz\model')
from model.schema import user_schema

#path2 = sys.path.insert(1,'D:\mongo_code\pymongo\Quiz\controller')

from controller import classes, userController

#path3 = sys.path.insert(1,'D:\mongo_code\pymongo\Quiz')
from db import client
from server import app




@app.route('/getData',methods = ['GET','POST'])
def play_game():
    if request.method==['GET']:
        return "hello"


