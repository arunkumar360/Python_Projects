questions = ('How many elements are in the peroidic table?:',
             'Whch animal lays the largest eggs?:',
             "What is the most abuntant gas in the earth's atmosphere?:",
             'How many bones are in the human body?:',
             'Which planet in the solar system is the hottest?:')

options = (('A.116','B.117','C.118','D.119'),
           ('A.Whale','B.Crocodile','C.Elephant','D.Ostrich'),
           ('A.Nitrogen','B.Oxygent','C.Carbon-dioxide','D.Hydrogen'),
           ('A.206','B.207','C.208','D.209'),
           ('A.Mercury','B.Venus','C.Earth','D.Mars'))


answers = ('C','D','A','A','B')

guesses = []
score = 0
question_num =  0  



for question in questions:
    print("----------------------------------")

    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("CORRECT!")
        score += 1
    else:
        print("INCORRECT!")
        print(f'{answers[question_num]} is the answer!')

    question_num += 1

print("----------------------------------")

print("            RESULT              ")

print("----------------------------------")


print("Answers: ",end = "")
for answer in answers:
    print(answer,end=" ")

print()

print("Guesses: ",end="")
for guess in guesses:
    print(guess,end=" ")

score = int((score / len(questions)) * 100)
print()
print(f'Your score is: {score}%')