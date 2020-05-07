#!/usr/bin/python3.8

import random


print("Hello! What is your name?")
username = input()
print(f"Well, {username}, let's play rock-paper-scissor game\nThe game ends when one of us get 3 wins")
print("Press 1 to choose rock, press 2 to choose paper, press 3 for scissor")
options = {1:'rock', 2:'paper', 3:'scissor'}
comWins = 0
userWins = 0
while comWins < 3 and userWins < 3: 
    while True:
        pickNum = int(input("Pick yours:"))
        try:
            if len(pickNum) > 1:
                print("You can only input 1 number")
            elif len(pickNum) == 0:
                print("You didn't input anything")
            else:
                break
        except ValueError:
            print("That is not a number, please enter a valid number!!")
    comPick = options[random.randint(1,3)] 
    userPick = options[pickNum]
    print(f"{userPick}(you) vs {comPick}(com)")
    if comPick == userPick:
        print("Draw")
    elif comPick == "rock":
        if userPick == "paper":
            print("You win")
            userWins += 1
        else:
            print("Computer wins")
            comWins += 1
    elif comPick == "paper":
        if userPick == "scissor":
            print("You win")
            userWins += 1
        else:
            print("Computer wins")
            comWins += 1
    elif comPick == "scissor":
        if userPick == "rock":
            print("You win")
            userWins += 1
        else:
            print("Computer wins")
            comWins += 1
    print("Computer's wins:",comWins)
    print("Your wins:",userWins)