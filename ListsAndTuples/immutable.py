#!/usr/bin/env python3


# The ID for an object may be different each time you
# run teh program, but while your program's running, the object will have the same id.
# If python has to destroy the object and re-create it, hen its ID will change.
# That gives us a good way to tell if an object is changed, or if Python has to create a new object.


# result = True
# another_result = result
# print(id(result))
# print(id(another_result))

# result = False
# print(id(result))


result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

result += "ish"
print(id(result))
print(id(another_result))


