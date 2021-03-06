import random
import sys


class Player:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.score = 0
    
    def update_score(self):
        self.clear()
        self.write("Score: {}".format(self.score), font=("Arial", 14, "normal"))

    def change_score(self, points):
        self.score += points
        self.update_score()

player = Player

#Player decides whether to be a goalkeeper or a shooter

#Program decides where goalkeeper attempts to save
# options=["TL ", "BL" , "M" , "TR", "BR"]
# computerOption = random.choice(options)

# #Player decides where they want to shoot 
# userOption = input("Where would you like to shoot?")

#Score is updated after every attempt

#After 5 attempts the game ends letting player know if they won or failed. 
