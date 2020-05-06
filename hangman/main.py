#!/usr/bin/python3.8

import random
import re


print("Hello! What is your name?")
username = input()
print(f"Hi {username}, This is a Hangman game\nYou only have 6 chances to guess wrong letter")
print()
with open("words.txt", "r") as f:
    output = f.read().split("\n")
randomWord = random.choice(output)
hiddenWord = list('_' * len(randomWord))  # Mystery word that pops up
misses = '' # Wrong guess
chances = 6
while chances >= 0:
    print(hiddenWord)
    print(f"Misses: {misses},       {chances} chances left")
    while True:
        guess = input("Enter a character:")
        lenInput = len(guess)
        if lenInput == 0:
            print("You didn't input anything")
        elif lenInput > 1:
            print("You can only input 1 character")
        elif not guess.isalpha():
            print("That is not an alphabet")
        else:
            break
    print()
    print()
    rightGuess = [m.start() for m in re.finditer(guess, randomWord)]    # Get index of the character that guessed 
    if rightGuess:
        for r in rightGuess:
            hiddenWord[r] = guess   # Change _ to the guessed character
        if '_' not in hiddenWord:
            print(hiddenWord)
            print(f"Congratulaions!! You did it!\nThe secret word is \"{randomWord}\"")
            break
    elif guess not in misses:
        chances -= 1
        misses += guess
        if chances < 0:
            print("Sorry, you lose")
        else:
            print(f"Whoooopss, you wrong! {chances} wrong guess chances left.")
            print()
    else:
        print("You've chosen it, and that is wrong")
        print()