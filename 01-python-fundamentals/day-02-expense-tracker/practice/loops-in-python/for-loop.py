# For Loop in python
# For loop is used to iterating ove sequences like list, tuple, dict, sets or strings
# String
# for x in "banana":
#     print(x)

# List 
# for x in ["alex", "flivian", "david"]:
#     print(x)

# Tuple
# for x in ("cake", "yought", "ice-cream"):
#     print(x)

# Sets
# for x in {"cow", "dog", "cat"}:
#     print(x)

# Dictionary
# details = {
#     "name": "flivian",
#     "password": "flivo123",
#     "role":"admin"
# }
# for x in details.keys():
#     if x == "password":
#         continue
#     print(x)

"""
Coding Challenge
1. Create a list called fruits with: "apple", "banana", "cherry"
2. Write a for loop that prints each item in fruits
3. Use break to stop the loop when the item is "banana"
"""
# Implementation
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
