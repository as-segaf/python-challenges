#!/usr/bin/python3.8

import random

rand_num = random.randint(1,20)
input_num = 0
attempts = 0

print("Hello! What is your name?")
username = input()
print(f"Well, {username}, I am thinking of a number between 1 and 20\nCan you guess it?")

while rand_num != input_num:
    input_num = int(input("Guess a number between 1 and 20 until you get right:"))
    if input_num > rand_num:
        print("No, it's too big")
    elif input_num < rand_num:
        print("Nope, too small")
    attempts+=1
print(f"Good job {username} that's {input_num}, you guessed in {attempts} attempts")
