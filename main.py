import random

# from flask import Flask

# #add variable dunder name
# app = Flask(__name__)
# app.run(debug=True, host='0.0.0.0') 

#add best of five code

#Player enters name
name = input('What is your name?')
start = "Let's play Louisville FC Soccer, " + name + '!'
print(start)

score = 0
for i in range(0,5):

    options=["TL","BL","M","TR","BR"]
    computerOption = random.choice(options)

    userOption = input("Where would you like to shoot? (TL, BL, M, TR, or BR)")

    if computerOption == userOption:
        print("Goal Keeper Lundt blocked the penalty kick.")

    else: 
        print("You have scored a goal!")
        score += 1
        print("Your score:" + str(score))


