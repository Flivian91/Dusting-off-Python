# Sets in python
# -sets are collection of unordered, uncahngable* and unindexed
# -sets are written using cury brackets
thisset = {"apple", "banana", "cherry", "apple"}
# print(type(thisset))

# 01 - Accessing the set
# using for loop
# for x in thisset:
#     print(x)
# using in keyword
# print("banana"  in thisset)

# 02 - Adding set items
# thisset.add("orange")
# print(thisset)
# newset = {"flivo", "mweni", "cane"}
# thisset.update(newset)
# print(thisset)

# 03 - Join sets items
newset = {1, 2, 3, 4}
moreset = {2, 4}
# - union() and update() methods joins all items form the both sets.
# thisset.union(newset)
# setupdated = thisset.union(newset)
# thisset.update(newset)
# print(thisset)
# print(setupdated)

# - intersection() method keeps only the duplicates
# intersectionset = newset.intersection(moreset)
# print(intersectionset)

# - difference() method keeps the items form the first set which are not in the other set(s)
# differenceset = newset.difference(moreset)
# print(differenceset)

# - symmetric_difference() method keeps all the items except the duplicate.
# symmetricset = newset.symmetric_difference(moreset)
# print(symmetricset)

# 04 - frozenset i python
# frozen = frozenset({"admin", "reader", "viewer"})
# print(type(frozen))

"""
Coding Challenge
Inside the editor, complete the following steps:
1. Create a set called colors with the values "red", "green", "blue"
2. Print the set
3. Add "yellow" to the set using add()
4. Remove "green" from the set using discard()
5. Print the number of items using len()
"""
# Implementation
colors = {"red", "green", "blue"}
print(colors)
colors.add("yellow")
colors.discard("green")
print(len(colors))