#!/usr/bin/env python3


#-------------------------------------
# This is a good example of lists iteration with while loops
# user input, list length, f'string concatenation
# str_list = []
# num_list = []

# while len(str_list) < 5:
#     ask_user_for_str = input("Enter a string: ")
#     str_list.append(ask_user_for_str)

# while len(num_list) < 3:
#     ask_user_for_num = int(input("Enter a number: "))
#     num_list.append(ask_user_for_num)


# print(f"{str_list[num_list[0]]}{str_list[num_list[1]]}{str_list[num_list[2]]}")
# -----------------------------------------------------------------------------



# simple script, ----------------------------------------------
# user_int = input("Enter an integer: ")

# if user_int.isdigit():
#     user_name = input("What is your name? ")
#     print(user_name.upper())
# else:
#     print(user_int.capitalize())
#-----------------------------------------------------------




# check if a word is in a sentence-------------------------------------
# userFirstWord = input("Enter a word: ")
# userSecondWord = input("Enter another word: ") 

# if userFirstWord in userSecondWord:
#     print("The first word is contained in the second one")
# else:
#     print("The first word isn't contained in the second one")
#-------------------------------------------------------------------------


# count how many words are in a sentence ----------------------------------------

# sentence = input("Enter a sentence: ")

# words = sentence.split(" ")
# number_of_words = len(words)

# print(f"There are {number_of_words} words in this sentence")
# ---------------------------------------------------------------------------------


# iterate through an array by item-------------------------
# lst = ["time", "is", "the", "best"]
# string = "...."
# tupl = ("and", "he", "is", "great")

# for i in range(len(lst)):
#     print(lst[i])

# for j in range(len(string)):
#     print(string[j])

# for k in range(len(tupl)):
#     print(tupl[k])
#-----------------------------------------------------------


# print all matching characters ----------------------------------------
# string1 = "aabbcsdw"
# string2 = "abbbcsdd"

# for i in range(len(string1)):
#     char1 = string1[i]
#     char2 = string2[i]

#     if char1 == char2:
#         print(char1)

# ----------------------------------------------------------------------


# print numbers divisible by two and odd indexes ---------------------------------
# lst = [45, 24, 22, 1, 45, 2, 12, 13, 16, 10, 0, -7]

# for i in range(len(lst)):
#     num = lst[i]
#     if num % 2 == 0 and i % 2 != 0:
#         print(num)
    
# -----------------------------------------------------------------------------




lst = [[2, 3, 4], [-2, -4, 0], [1, 2], [1, 1, 1, 5, 6], [0, 9, 8, 7]]

# Write your code here.
for inner_list in lst:
    sum_inner_lst = 0

    for item in inner_list:
        sum_inner_lst += item
    
    print(sum_inner_lst)

    






