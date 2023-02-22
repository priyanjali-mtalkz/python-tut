from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def mainPage():
    return jsonify({"Status" : "Working Successfully"})

from route import *
if __name__ == '__main__':
    app.run(debug = True, port = 9001)


