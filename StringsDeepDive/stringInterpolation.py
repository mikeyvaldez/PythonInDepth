#!/usr/bin/env python3

# This is an example of string interpolation
# it is not recommended to be used when developing in python 3
# string interpolation will no longer be supported in later versions
# it is being deprecated and will be removed from the language at some point

age = 24
print("My age is %d years" % age)


major = "years"
minor = "months"
print("My age is %d %s, %d %s" % (age, major, 6, minor))
print("PI is approximatley %f" % (22 / 7))
print("PI is approximatley %60.50f" % (22 / 7))