#!/usr/bin/env python3





name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)



if age >= 18:   # essentially the same as code block below
    print("You are old enough to vote")
    print("Please put an X in the box")
else:
    print("Please come back in {0} years".format(18 - age))

if age < 18:   # essentially the same as the code block above
    print("Please come back in {0} years".format(18 - age))
else:
    print("You are old enough to vote")
    print("Please put an X in the box")