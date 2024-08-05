#!/usr/bin/env python3



name = input("What is your name:\n")
age = int(input("How old are you?\n"))

if 18 <= age < 31:
    print("Welcome to the holiday {0}!".format(name))
else:
    print("You gotta leave.....")