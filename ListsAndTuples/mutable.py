#!/usr/bin/env python3

# Lists are mutable

shopping_list = ["computer",
                 "monitor",
                 "keyboard",
                 "mouse",
                 "power supply"
                 ]


another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))