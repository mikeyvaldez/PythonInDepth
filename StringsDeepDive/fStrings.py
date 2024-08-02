#!/usr/bin/env python3

#########################################################
# f-strings wont work with python 3.4 or earlier versions#
#########################################################

print(f"Pi is approzimately {22 /7:12.50f}")

pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")