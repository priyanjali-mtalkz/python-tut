def game_begins():
    user_answers = []
    answer = 0
    question_num = 1

    for question in questions:
        print("Question"+str(question_num)+": ")
        print(question)
        
        print("OPTIONS:",end='\n')
        for option in options[question_num-1]:
            print(option)

        user_ans = input("Choose an Option : (A B C or D)").upper()
        user_answers.append(user_ans)

        answer += check_answers(questions.get(question),user_ans)

        question_num+=1

    score(answer)

def check_answers(correct_ans,user_ans):
    print(user_ans)
    print(correct_ans)
    if(correct_ans == user_ans):
        print("  CORRECT!!  ")
        return 1
    else:
        print("  INCORRECT!!  ")
        return 0

def score(answers):
    print("RESULT: ")
    x = int((answers/len(questions))*100)
    print("Your final score is "+str(x)+"%")



def play_again():
    user_response = input("Do you want to play again?: (Yes or No)").upper()
    if (user_response == "YES"):
        return 1
    else:
        return 0


        




questions = {
    "What's the capital of Norway": "D",
    "What's the state capital of Texas, USA" : "D",
    "When was the first public version of Python released?" : "A",
    "What's the name of Python's sorting algorithm" : "A"
}

options = [
    ["A.Stockholm", "B.Copenhagen", "C.Helsinki", "D. Oslo"  ],
    ["A.Harrisburg", "B. Houston", "C. Columbia" , "D. Austin"],
    ["A.January 1991", "B.October 2000", "C.December 2008","D.January 1994"],
    ["A.Bubble sort", "B. Insertion sort", "C. Time Sort", "D. Quick sort"]
]

game_begins()

while(play_again()):
    game_begins()

print("  Thankyou!!  ")
