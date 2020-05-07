#!/usr/bin/python3.8

import random


randNumber = random.randint(1,20)
inputNumber = 0
attempts = 0

# Welcoming user
print("Hello! What is your name?")
username = input()
print(f"Well, {username}, I am thinking of a number between 1 and 20\nCan you guess it?")
print()

# Game limit
while randNumber != inputNumber:
    # Input limit
    while True:
        try:
            inputNumber = int(input("Guess a number between 1 and 20 until you get right:"))
            
            if inputNumber == 0:
                print("You didn't input anything")
        except ValueError:
            print("That is not a valid number")

    if inputNumber > randNumber:
        print("No, it's too big")
    elif inputNumber < randNumber:
        print("Nope, too small")
    attempts+=1

print(f"Good job {username} that's {inputNumber}, you guessed in {attempts} attempts")