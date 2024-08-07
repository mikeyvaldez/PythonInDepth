#!/usr/bin/env python3


# for i in range(10):
#     print("i is now {}".format(i))


# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1


available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: \n")

print("aren't you glad you got out of there?")