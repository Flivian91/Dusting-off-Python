# Python Tuples
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# To create a tuple using a tuple() constructor
# newtuple = tuple(("flivian", "mike", 20, False))
# print(type(newtuple))

# 01 - Access Tuple Items
# print(thistuple[1])
# print(thistuple[2:5]) #the search start at 2(included) and end at 5(excluded)
# print(thistuple[-3:-1]) #the search start at -4(included) and end at -1(excluded)

# 02 - Update a Tuple
# To update(add, change, remove) item in a tuple first change the tuple to a list, change the list, then convert the lit back to a tuple
# to change item
# list = list(thistuple)
# list[0] = "carrot"
# newtuple = tuple(list)
# print(newtuple)
# adding item in a tuple
# list = list(thistuple)
# list.append("flivian")
# newtuple = tuple(list)
# print(newtuple)
# adding a tuple to a tuple

# Unpacking tuple in python
# (fli, *mwi, rest) = thistuple
# print(fli)
# print(mwi)
# print(rest) #the rest are collected into a list
# thistuple.index()
"""
Coding Challenge
Inside the editor, complete the following steps:
1. Create a tuple called fruits with the values "apple", "banana", "cherry"
2. Print the second item in the tuple
3. Print the number of items using len()
4. Unpack the tuple into three variables a, b, c
5. Print the variable b
"""
# Implementation
fruits = ("apple", "banana", "cherry")
print(fruits[1])
print(len(fruits))
(a, b, c) = fruits
print(b)
