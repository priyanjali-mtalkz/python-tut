import pymongo 
import time

client = pymongo.MongoClient("mongodb://localhost:27017")
print("Connection Successful")

db = client['Quiz']
collection3 = db['Questions']

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
    "option3" : "C. Bill Gates",
    "option4" : "D. Mark Zuckerburg",
    "answer" : "A",
    "hint" : "Distinguished Engineer at Microsoft",
    "explanation" : """He is a Dutch programmer best known as the 
    creator of the Python programming language, 
    for which he was the benevolent dictator for life (BDFL) 
    until he stepped down from the position on 12 July 2018"""
}]

#x = collection3.insert_many(ques)

#x=collection3.delete_many({})

collection1 = db['EasyQuestions']

easy_ques = [{
    "question" : "How many legs does a spider have?",
    "option1" : "A: Six",
    "option2" : "B: Ten",
    "option3" : "C: Eight",
    "option4" : "D: Four",
    "answer" : "C",
    "hint" : "Spiders belong to the class of arachnids.",
    "explanation" : """Spiders belong to the class of arachnids.
        All arachnids, have eight legs.
        Though spider falls under the phylum of Arthropoda
        which has only 6 legs the spiders have 8 legs.
        Spiders fall under the phylum Arthropoda and hence are related to crabs and prawns."""
},
{
    "question" : "What is the name of the toy cowboy in Toy Story?",
    "option1" : "A: Stella",
    "option2" : "B: Woody",
    "option3" : "C: Clara",
    "option4" : "D: Stanley",
    "answer" : "B",
    "hint" : "Cowboy doll appears in the Disney Pixar Toy Story franchise",
    "explanation" : """In the films, Woody is the main protagonist, alongside Buzz Lightyear. 
    He is primarily voiced by Tom Hanks, who voices him in the Toy Story films, short films,
    and TV specials. Tom Hanks' brother, 
    Jim Hanks, voices him in Lamp Life, video games,
    attractions, and other merchandise"""
},
{
    "question" : "What is the color of an emerald?",
    "option1" : "A: Red",
    "option2" : "B: Green",
    "option3" : "C: Blue",
    "option4" : "D: Black",
    "answer" : "B",
    "hint" : "It is considered a classic color that can symbolize refinement, wealth and royalty",
    "explanation" : """Emerald is a shade of green, 
    a color that symbolizes balance and harmony. 
    Green has strong associations with 
    nature and the environment and is seen 
    as the color of luck, freshness and renewal."""
},
{
    "question" : "Where does the President of the United States live while in office?",
    "option1" : "A: The White House",
    "option2" : "B: President's House",
    "option3" : "C: PM Office",
    "option4" : "D: Capital house",
    "answer" : "A",
    "hint" : "It is located at 1600 Pennsylvania Avenue NW in Washington, D.C",
    "explanation" : """The White House is the official residence and workplace of the 
    president of the United States."""
},
{
    "question" : "Where does Santa Claus live?",
    "option1" : "A: The South Pole",
    "option2" : "B: The North Pole",
    "option3" : "C: The East Pole",
    "option4" : "D: The West Pole",
    "answer" : "B",
    "hint" : "The exact location of Santa Claus's original home is known as Ear Fell or Korvatunturi",
    "explanation" : """Santa Claus is said to live at the North Pole with his wife, 
    where he spends the year making toys with the help of his elves. 
    There he receives letters from children asking for Christmas gifts."""
}]

#a = collection1.delete_many({})
#a = collection1.insert_many(easy_ques)

collection2 = db['MediumQuestions']
medium_ques = [{
    "question" : "What year did the Titanic sink in the Atlantic Ocean on 15 April, on its maiden voyage from Southampton?",
    "option1" : "A: 1932",
    "option2" : "B: 1902",
    "option3" : "C: 1912",
    "option4" : "D: 1905",
    "answer" : "C",
    "hint" : "RMS Titanic was a British passenger liner, operated by the White Star Line, which sank in the North Atlantic Ocean",
    "explanation" : """The RMS Titanic, a luxury steamship, 
    sank in the early hours of April 15, 1912, 
    off the coast of Newfoundland in the North Atlantic after 
    sideswiping an iceberg during its maiden voyage. 
    Of the 2,240 passengers and crew on board, 
    more than 1,500 lost their lives in the disaster."""
},
{
    "question" : " What is the capital of Portugal?",
    "option1" : "A: Lisbon",
    "option2" : "B: Coimbra",
    "option3" : "C: Viana do Castelo",
    "option4" : "D: Castelo Branco",
    "answer" : "A",
    "hint" : "Its two archipelagos form two autonomous regions with their own regional governments.",
    "explanation" : """Lisbon is the capital and the largest city of Portugal. It is the westernmost large city located in continental Europe, 
    as well as its westernmost capital city and the 
    only one along the Atlantic coast."""
},
{
    "question" : "What is the world’s smallest bird?",
    "option1" : "A: Songbirds",
    "option2" : "B: American Goldfinch",
    "option3" : "C: Bee Hummingbird",
    "option4" : "D: Common Starling",
    "answer" : "C",
    "hint" : "They weigh less than two grams — less than a dime.",
    "explanation" : """The Bee Hummingbird, which is found only in Cuba, is an absolute miniature, 
    even among hummingbirds. It measures a mere two and a quarter inches long"""
},
{
    "question" : "What is the lifespan of a dragonfly?",
    "option1" : "A: 48 hours",
    "option2" : "B: 24 hours",
    "option3" : "C: 12 hours",
    "option4" : "D: 6 hours",
    "answer" : "B",
    "hint" : "A dragonfly is a flying insect belonging to the infraorder Anisoptera below the order Odonata",
    "explanation" : """Dragonflies have a short life span, with many living for only 1 to 2 weeks, 
    although some can live up to 8 weeks. 
    Because of their short life span, dragonflies 
    spend most of their time eating or mating."""
},
{
    "question" : "Who invented the tin can for preserving food in 1810?",
    "option1" : "A: Albert Einstein",
    "option2" : "B: Georg Simon Ohm",
    "option3" : "C: Peter Durand",
    "option4" : "D: John Dalton",
    "answer" : "C",
    "hint" : "He was an English merchant who is widely credited with receiving the first patent for the idea of preserving food using tin cans.",
    "explanation" : """In 1810 Peter Durand of England patented the use of tin-coated iron cans 
    instead of bottles, and by 1820 he was supplying 
    canned food to the Royal Navy in large quantities."""
}]
#b = collection2.delete_many({})
#b = collection2.insert_many(medium_ques)

def level(response):
    if(response == "EASY"):
        return collection1
    elif(response == "MEDIUM"):
        return collection2
    elif(response == "HARD"):
        return collection3
        

guess=0

user_level = input("Choose your choice of level: (EASY, MEDIUM OR HARD)").upper()
coll = level(user_level)


def game_begins():
    user_answers = []
    question_num = 1
    global guess
    guess=0
    for questions in coll.find():
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

        guess += check_answers(questions['answer'],user_answer)
        question_num+=1
  

def check_answers(correct_ans,user_ans):
    if(correct_ans == user_ans):

        print("  CORRECT!!  ")
        print("----------------")
        return 1
    else:
        print("  INCORRECT!!  ")
        print("----------------")
        return 0

        
def score(g):
    x = ((g/5)*100)
    return x

def play_again():
    user_response = input("Do you want to play again?: (Yes or No)").upper()
    if (user_response == "YES"):
        return 1
    else:
        return 0



collection4 = db['UserDetails']
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
    user_id[data4] = user_level

    arr.append(user_id)
    user_id = {}

collection4.insert_many(arr)
#y=collection4.delete_many({})



while(play_again()):
    game_begins()
print("----------------")
print("   Thankyou!!   ")
print("----------------")