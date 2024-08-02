#!/usr/bin/env python3


string1 = "he's "
string2 = "probably "
string3 = "pinging "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)  # these two lines of code give the same output
print("he's " "probably " "pinging " "for the " "fjords")

print("Hello " * 5)  # prints the word hello 5 times

# print("hello " * 5) # throws an error

print("Hello " * (5 + 4))    # prints the word hello 9 times
print("Hello " * 5 + "4")   # prints the word hello 5 times then appends the number 4 to the end 


today = "friday"
print("day" in today)    # True
print("fri" in today)    # True
print("thur" in today)    # False
print("parrot" in "fjord")    # False
