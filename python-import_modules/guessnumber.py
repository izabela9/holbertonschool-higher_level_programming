#!/usr/bin/python3
import random
def guess_the_number():
    n = random.randint(1,20)
    guess = int(input("Enter any number:"))
    while n != guess:
        if guess < n:
            print("Too low")
            guess = int(input("Enter number again:"))
        elif guess > n:
            print("Too high")
            guess = int(input("Enter number again:"))
        
    print("Congratulations! The right number is: {}".format(guess))

guess_the_number()