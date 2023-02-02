import pymongo 
import time

client = pymongo.MongoClient("mongodb://localhost:27017")
print("Connection Successful")

db = client['Quiz']

collection1 = db['EasyQuestions']

collection2 = db['MediumQuestions']

collection3 = db['Questions']

collection4 = db['UserDetails']


class Quiz:
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
    coll = level(response)


    def check_answers(self,correct_ans,user_ans):
        if(correct_ans == user_ans):

            print("  CORRECT!!  ")
            print("----------------")
            return 1
        else:
            print("  INCORRECT!!  ")
            print("----------------")
            return 0


    def game_begins(self):

        user_answers = []
        question_num = 1
        global guess
        guess=0

        for questions in self.coll.find():
            print("Question "+str(question_num)+": ")
            print(questions['question'])

            print("   OPTIONS:   ",end='\n')
            print(questions['option1'])
            print(questions['option2'])
            print(questions['option3'])
            print(questions['option4'])

            user_answer = input("Choose an Option : (A B C or D) or type hint to get one").upper()
            if(user_answer == "HINT"):
                print("----------------")
                print("     HINT!!      ")
                print("----------------")
                print(questions['hint'])
                user_answer = input("Choose an Option : (A B C or D)").upper()
            user_answers.append(user_answer)

            print("   EXPLANATION!!    ")
            print("----------------")
            print(questions['explanation'])

            print("----------------")

            guess += self.check_answers(questions['answer'],user_answer)
            question_num+=1


   

    def score(g):
        x = ((g/5)*100)
        return x

    def play_again():
        user_response = input("Do you want to play again?: (Yes or No)").upper()
        if (user_response == "YES"):
            return 1
        else:
            return 0
    users = int(input("Enter the number of users"))    
    arr = []
    user_id = {}


    for i in range(users):
        data1 = "UserID"
        num = input("Enter your mobile no.")
        user_id[data1] = num

        startTime = time.time()

        game_begins()

        endTime = time.time()
        timetaken = endTime - startTime

        data2 = "Score"
        user_id[data2] = score(guess)

        data3 = "Timetaken"
        user_id[data3] = timetaken

        data4 = "Level"
        user_id[data4] = level(response)

        arr.append(user_id)
        user_id = {}

    collection4.insert_many(arr)
    #y=collection4.delete_many({})

    
    while(play_again()):
        game_begins()
    print("----------------")
    print("   Thankyou!!   ")
    print("----------------")


