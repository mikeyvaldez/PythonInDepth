#!/usr/bin/env python3


letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[::-1]   # alphabet backwards
print(backwards)

# create a slice that produces the characters qpo
print(letters[16:13:-1])

# slice the string to produce edcba
print(letters[4::-1])

# slice the string to produce the last 8 characters, in reverse order
print(letters[:-9:-1])

# slice the string to produce wxyz
print(letters[-4:])

# slice the string to produce the last letter
print(letters[-1:])

# slice the string to produce the first letter
print(letters[:1])
print(letters[0])