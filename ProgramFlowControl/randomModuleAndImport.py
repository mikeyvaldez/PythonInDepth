#!/usr/bin/env python3


import random

highest = 100
answer = random.randint(1, highest)
print(answer)   # todo: remove after testing

print("Please guess number between 1 and 10: ".format(highest))
guess = 0     # initialize toany number that doesn't equal the answer
while guess != answer:
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it!")
        break
    else:
        if guess < answer:
            print("Please guess higher")            
        else:      # guess must be greater than answer
            print("Please guess lower")    