from flask import Flask,jsonify,request

app = Flask(__name__)


questions = [
            {
                "ques" : "Who created Python?",
                "options" : {
                        "option1" : "A. Guido van Rossum",
                        "option2" : "B. Elon Musk ",
                        "option3" : "C. Bill Gates",
                        "option4" : "D. Mark Zuckerburg"
                }
                ,
                "answer" : "A",
                "hint" : "Distinguished Engineer at Microsoft",
                "explanation" : "He is a Dutch programmer best known as the creator of the Python programming language, for which he was the benevolent dictator for life (BDFL) until he stepped down from the position on 12 July 2018"
            },
            {
                "ques" : "What's the name of Python's sorting algorithm",
                "options" :
                    {
                        "option1" : "A.Bubble sort",
                        "option2" :  "B. Insertion sort",
                        "option3" : "C. Time Sort",
                        "option4" : "D. Quick sort"

                    }
                ,
                "answer" : "A",
                "hint" : "There may be multiple correct answers",
                "explanation" : "Sorting is defined as an arrangement of data in a certain order.Sorting techniques are used to arrange data(mostly numerical) in an ascending or descending order."

            }
        ]
@app.route('/questions/add',methods = ['GET','POST'])

def question():
    if(request.method == 'GET'):
        return jsonify(questions)
    else:
        request_data = request.get_json()
        new_ques = {"ques":request_data["ques"], "answer" : [], "options":[], "hint" : request_data["hint"], "explanation" : request_data["explanation"]}
        questions.append(new_ques)
        return new_ques, 201

@app.route('/questions/add/<string:question>/options',methods=['POST'])
def create_answer(question):
    request_data = request.get_json()
    for q in questions:
        
            if q["ques"] == question:
                new_ele = {"option1":request_data["option1"], "option2" : request_data["option2"], "option3" : request_data["option3"], "option4" : request_data["option4"]}
                q["options"] = new_ele
                return new_ele, 201
    return questions, 201



if __name__ == '__main__':
    app.run(debug=True) 

