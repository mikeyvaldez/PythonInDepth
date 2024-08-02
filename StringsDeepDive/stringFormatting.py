#!/usr/bin/env python3

# you can use colons(for spacing) to format the output to be more legible

for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i **3))


print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))


print()

print("Pi is approximately {0:12}".format(22 / 7))          # defaults to printing 15 decimal places
print("Pi is approximately {0:12f}".format(22 / 7))         # f represents float and defaults to print precisely 6 digits
print("Pi is approximately {0:12.50f}".format(22 / 7))      # also a float but prints 50 decimal places
print("Pi is approximately {0:52.50f}".format(22 / 7))      # since in python precision is more important than fied width so it prints 50 decimal places
print("Pi is approximately {0:62.50f}".format(22 / 7))      # in this line the field is affected aswell
print("Pi is approximately {0:72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7))


for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".f.ormat(i, i ** 2, i ** 3))