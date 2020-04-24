#!/usr/bin/python3.8

import random

print("Hello! What is your name?")
username = input()
print(f"Well, {username}, let's play rock-paper-scissor game\nThe game ends when one of us get 3 wins")
print("Press 1 to choose rock, press 2 to choose paper, press 3 for scissor")
options = {1:'rock',2:'paper',3:'scissor'}
com_wins, user_wins = 0,0

while com_wins < 3 and user_wins < 3: 
    comp_pick = options[random.randint(1,3)] 
    pick_num = int(input("Pick yours:"))
    user_pick = options[pick_num]
    print(f"{user_pick}(you) vs {comp_pick}(com)")

    if comp_pick == user_pick:
        print("Draw")
    elif comp_pick == 'rock' and user_pick == 'scissor':
        print("Computer wins")
        com_wins+=1
    elif comp_pick == 'rock' and user_pick == 'paper':
        print("You win")
        user_wins+=1
    elif comp_pick == 'paper' and user_pick == 'rock':
        print("Computer wins")
        com_wins+=1
    elif comp_pick == 'paper' and user_pick == 'scissor':
        print("You win")
        user_wins+=1
    elif comp_pick == 'scissor' and user_pick == 'paper':
        print("Computer wins")
        com_wins+=1
    elif comp_pick == 'scissor' and user_pick == 'rock':
        print("You win")
        user_wins+=1
    print("Computer's wins:",com_wins)
    print("Your wins:",user_wins)

    if comp_pick == user_pick:
        print("Draw")
    elif comp_pick == "rock":
        if user_pick == "paper":
            print("You win")
            user_wins+=1
        else:
            print("Computer wins")
            com_wins+=1
    elif comp_pick == "paper":
        if user_pick == "scissor":
            print("You win")
            user_wins+=1
        else:
            print("Computer wins")
            com_wins+=1
    elif comp_pick == "scissor":
        if user_pick == "papr":
            print("You win")
            usr_wins+=1
        else:
            print("Computer wins")
            com_wins+=1

