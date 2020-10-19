import random
import sys

#Player enters name
class Player:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.score = 0

#Player decides whether to be a goalkeeper or a shooter

#Program decides where goalkeeper attempts to save

#Player decides where they want to shoot 

#Score is updated after every attempt

    def update_score(self):
        self.clear()
        self.write("Score: {}".format(self.score), font=("Arial", 14, "normal"))

    def change_score(self, points):
        self.score += points
        self.update_score()

#After 5 attempts the game ends letting player know if they won or failed. 
