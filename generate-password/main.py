#!/usr/bin/python3.8

import string
import random


print("Hello! What is your name?")
username = input()
print(f"Hi, {username}, This is a random password generator")

while True:
    try:
        print("How long do you want your password to be?")
        passLen = int(input('Enter a number:'))

        if passLen < 6:
            print("Password must be at least 6 characters!")
        else:
            while True:
                try:
                    print("How many letters do you want in your password?")
                    lettersCount = int(input("Enter a number:"))

                    if lettersCount > passLen:
                        print(f"It exceeds the password length, max {passLen}")
                    elif lettersCount == passLen:
                        numbersCount = 0
                        break
                    else:
                        while True:
                            try:
                                print("How many numbers do you want in your password?")
                                numbersCount = int(input("Enter a number:"))

                                if numbersCount > passLen-lettersCount:
                                    print(f"You only have {passLen-lettersCount} remaining characters!")
                                else:
                                    break
                            except ValueError:
                                print("This is not a number, please enter a valid number!")
                        break
                except ValueError:
                    print("This is not a number, please enter a valid number!")
            break
    except ValueError:
        print("This is not a number, please enter a valid number!")

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

password = ''.join(random.sample(letters, lettersCount))
password += ''.join(random.sample(numbers, numbersCount))
password += ''.join(random.sample(symbols, passLen-lettersCount-numbersCount))

password = ''.join(random.sample(password,len(password))) # Shuffle the string
print(f"Here is your password: {password}")