#!/usr/bin/env python3


quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""


# Extract all the capital letters from the quote above
capitals = ""

for char in quote:
    if char.isupper():
        capitals += char

print(capitals)