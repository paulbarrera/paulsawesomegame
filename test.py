
import random
import sys 
import time

class soccerShootout:
    player_team = ""
    virtual_player_team = ""
    player_shootout_blocks = 0
    player_shootout_goals = 0
    count_player = 0
    virtual_player_shootout_goals = 0
    virtual_player_shootout_blocks = 0
    count_virtual_player = 0
    event_count = 0
 
    def increaseEventCount(): 
        soccerShootout.event_count += 1
    
    def increaseCountPlayer(): 
        soccerShootout.count_player += 1
        
    def increasePlayerShootoutGoals(): 
        soccerShootout.player_shootout_goals += 1
 
    def increasePlayerShootoutBlocks(): 
        soccerShootout.player_shootout_blocks += 1
 
    def increaseCountVirutalPlayer(): 
        soccerShootout.count_virtual_player += 1
        
    def increaseVirutalPlayerShootoutGoals(): 
        soccerShootout.virtual_player_shootout_goals += 1
 
    def increaseVirtualPlayerShootoutBlocks(): 
        soccerShootout.virtual_player_shootout_blocks += 1

    def soccerEvent():
        soccerShootout.increaseEventCount()
        pt = soccerShootout.player_team
        vpt = soccerShootout.virtual_player_team
        ec = soccerShootout.event_count
        print(f"Event: Soccer Shootout - {ec} ")
        print("Location: Los Angeles, California")
        print(f"\n{pt} vs. {vpt} ")
        print(f"You will represent {pt} and the opponent is {vpt}.")
        print("Let the soccer shootout begin!")
        
    def playerKicker():
        pt = soccerShootout.player_team
        print(f"\nYou will be representing {pt} in the shootout as a kicker.")
    
    def playerGoalie():
        pt = soccerShootout.player_team
        print(f"\nYou will be representing {pt} in the shootout as a goalie.")
        print("goalie")
        
    def playerShootoutKicks():
        soccerShootout.increaseCountPlayer()
        cp = soccerShootout.count_player
        pt = soccerShootout.player_team
        while (cp >= 1 and cp <= 5):
            time.sleep(1)
            print(f"\nSetting up for shootout kick {cp}. Where will you kick the ball? ")
            ball_kick = input("Please enter left, center, or right: ")
            ball_direction = ball_kick.upper()
            time.sleep(1)
            while (ball_direction != "LEFT" and ball_direction != "CENTER" and ball_direction != "RIGHT"):
                print("\nInvalid input.")
                ball_kick = input("Please enter left, center, or right: ")
                ball_direction = ball_kick.upper()
            directions = ["LEFT", "CENTER", "RIGHT"]
            for i in random.sample(directions, 1):
                kicker_location = i
            if ball_direction == kicker_location:
                soccerShootout.increasePlayerShootoutGoals()
                ipsg = soccerShootout.player_shootout_goals
                time.sleep(1)
                print(f"\nYou scored a goal at the {kicker_location} location.")
                print(f"{pt} has scored {ipsg} goal(s).")
                playerShootoutKicks()
            else:
                soccerShootout.increaseVirtualPlayerShootoutBlocks()
                time.sleep(1)
                print(f"\nThe goalie blocked the kick at the {kicker_location} location.")
                playerShootoutKicks()
        else:
            playerGoalie()
            virtualPlayerShootoutKicks()
    
    def virtualPlayerShootoutKicks():
        directions = ["LEFT", "CENTER", "RIGHT"]
        soccerShootout.increaseCountVirutalPlayer()
        cvp = soccerShootout.count_virtual_player
        vpt = soccerShootout.virtual_player_team
        while (cvp >= 1 and cvp <= 5):
            time.sleep(1)
            print(f"\nSetting up for shootout kick {cvp} for {vpt}. Where will you try to block the ball? ")
            ball_kick = input("Please enter left, center, or right: ")
            ball_direction = ball_kick.upper()
            time.sleep(1)
            while (ball_direction != "LEFT" and ball_direction != "CENTER" and ball_direction != "RIGHT"):
                print("\nInvalid input.")
                ball_kick = input("Please enter left, center, or right: ")
                ball_direction = ball_kick.upper()
            for i in random.sample(directions, 1):
                kicker_location = i
            if ball_direction == kicker_location:
                soccerShootout.increaseVirutalPlayerShootoutGoals()
                ivpsg = soccerShootout.virtual_player_shootout_goals
                time.sleep(1)
                print(f"\n{vpt} scored a goal at the {kicker_location} location.")
                print(f"{vpt} has scored {ivpsg} goal(s).")
                virtualPlayerShootoutKicks()
            else:
                pt = soccerShootout.player_team
                soccerShootout.increasePlayerShootoutBlocks()
                time.sleep(1)
                print(f"\n{pt} goalie blocked the kick at the {kicker_location} location.")
                virtualPlayerShootoutKicks()
        else:
            shootoutScore()
    
    def shootoutScore():
        vpt = soccerShootout.virtual_player_team
        pt = soccerShootout.player_team
        psg = soccerShootout.player_shootout_goals
        vpsg = soccerShootout.virtual_player_shootout_goals
        print(f"\n{pt} {psg} - {vpt} {vpsg} ")
        if psg == vpsg:
            print(f"\nThe shootout resulted in a tie.")
        elif psg > vpsg:
            print(f"\n{pt} Wins!!!")
        elif psg < vpsg:
            print(f"\n{vpt} Wins!!!")
        confirmPlay()
