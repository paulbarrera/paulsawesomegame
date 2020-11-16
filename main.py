
import random
import sys
import datetime
import time
import pickle
#Local time
now = datetime.datetime.now()
print ("USL EastCoast Time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#Player enters name
name = input("What is your name?: ")
print("Hi " + name)
start = "Welcome to Paul's Awesome Game, " + name + '!'
print(start)
print("Would you like to play soccer shootout?")
answer = input("Yes or No : ").lower()
if answer == "yes":
    print("You said yes, let's play!")   
elif answer == "no":
    print("You said, no! See you next time.")
    exit()
else:
    print("what was that? restart program")
    exit()

#Game routine with definite iteration
def soccer_game():
    for i in range(0,5):
        score = 0
        options=["TL","BL","M","TR","BR"]
        computerOption = random.choice(options)

        userOption = input("Where would you like to shoot? (TL, BL, M, TR, or BR)")

        if computerOption == userOption:
            print("Goal Keeper Lundt blocked the penalty kick.")

        else: 
            print("You have scored a goal!")
            score += 1
            print("Your score:" + str(score))

#end of code
playagain = 'yes'
while playagain == 'yes': 
    soccer_game()
    print('Do you want to play again? (yes or no)')
    playagain = input()