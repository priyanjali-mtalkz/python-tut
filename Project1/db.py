import pymongo 
import time

client = pymongo.MongoClient("mongodb://localhost:27017")
print("Connection Successful")

db = client['Quiz']
collection1 = db['Questions']

ques =[{
        "question" : "What's the capital of Norway",
        "option1" : "A.Stockholm",
        "option2" :  "B.Copenhagen", 
        "option3" : "C.Helsinki",
        "option4" :  "D. Oslo",        
        "answer" : "D",
        "hint" : "Lars Onsager, Jens Stoltenberg, Trygve Lie, and Børge Ousland.",
        "explanation" : """Oslo was founded as a city in the 11th century and established as a
    trading place. It became the capital of Norway in 1299. The city was
    destroyed by a fire in 1624 and rebuilt as Christiania, named in honor
    of the reigning king. The city was renamed back to Oslo in 1925."""
},
{
    "question" : "What's the state capital of Texas, USA",
    "option1" : "A.Harrisburg",
    "option2": "B. Houston",
    "option3" :  "C. Columbia", 
    "option4" :  "D. Austin",
    "answer" : "D",    
    "hint" : "SciPy is held there each year.",
    "explanation" : """Austin is named in honor of Stephen F. Austin. It was purpose-built to
    be the capital of Texas and was incorporated in December 1839. Houston,
    Harrisburg, Columbia, and Galveston are all earlier capitals of Texas."""
},
{
    "question" : "When was the first public version of Python released?",
    "option1" : "A.January 1991",
    "option2" :  "B.October 2000",
    "option3" :  "C.December 2008",
    "option4" : "D.January 1994",
    "answer" : "A",
    "hint" : "The first public version was labeled version 0.9.0.",
    "explanation" : """Guido van Rossum started work on Python in December 1989. He posted
    Python v0.9.0 to the alt.sources newsgroup in February 1991. Python
    reached version 1.0.0 in January 1994. The next major versions,
    Python 2.0 and Python 3.0, were released in October 2000 and December
    2008, respectively."""
},
{
    "question" : "What's the name of Python's sorting algorithm",
    "option1" : "A.Bubble sort",
    "option2" :  "B. Insertion sort",
    "option3" : "C. Time Sort",
    "option4" : "D. Quick sort",
    "answer" : "A",
    "hint" : "There may be multiple correct answers",
    "explanation" : """Sorting is defined as an arrangement of data in a certain order.
    Sorting techniques are used to arrange data(mostly numerical) 
    in an ascending or descending order."""
},
{
    "question" : "Who created Python?",
    "option1" : "A. Guido van Rossum",
    "option2" : "B. Elon Musk ",
    "option3" : " C. Bill Gates",
    "option4" : " D. Mark Zuckerburg",
    "answer" : "A",
    "hint" : "Distinguished Engineer at Microsoft",
    "explanation" : """He is a Dutch programmer best known as the 
    creator of the Python programming language, 
    for which he was the benevolent dictator for life (BDFL) 
    until he stepped down from the position on 12 July 2018"""
}]
print("Collection1 created")
#x = collection1.insert_many(ques)

#x=collection1.delete_many({})


g2 = 0
def game_begins():
    user_answers = []
    question_num = 1
    guesses = 0

    for questions in collection1.find():

        print("Question"+str(question_num)+": ")
        print(questions['question'])
        
        print("OPTIONS: ",end='\n')
        print(questions['option1'])
        print(questions['option2'])
        print(questions['option3'])
        print(questions['option4'])


        user_answer = input("Choose an Option : (A B C or D) or type hint to get one").upper()
        if(user_answer == "HINT"):
            print(questions['hint'])
            user_answer = input("Choose an Option : (A B C or D)").upper()
        user_answers.append(user_answer)
    
        print(questions['explanation'])


        guesses += check_answers(questions['answer'],user_answer)
    

        question_num+=1

    g2 = score(guesses) 

def check_answers(correct_ans,user_ans):
    if(correct_ans == user_ans):
        print("  CORRECT!!  ")
        return 1
    else:
        print("  INCORRECT!!  ")
        return 0

def score(guess):
    x = ((guess/5)*100)
    return x


def play_again():
    user_response = input("Do you want to play again?: (Yes or No)").upper()
    if (user_response == "YES"):
        return 1
    else:
        return 0

def totalTime():
    startTime = time.time()
    game_begins()
    endTime = time.time()
    timetaken = endTime - startTime
    return timetaken


collection2 = db['UserDetails']
users = int(input("Enter the number of users"))
arr = []
user_id = {}


for i in range(users):
    data1 = "UserID"
    num = input("Enter your mobile no.")
    user_id[data1] = num

    data2 = "Score"
    res = score(g2)
    user_id[data2] = res

    data3 = "Timetaken"
    timetaken = totalTime()
    user_id[data3] = timetaken

    arr.append(user_id)
    user_id = {}

collection2.insert_many(arr)

game_begins()

while(play_again()):
    game_begins()

print("   Thankyou!!   ")