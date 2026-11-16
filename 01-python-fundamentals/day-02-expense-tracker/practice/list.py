# LIST
# 01 - Creating a list
thislist = ["apple", "Banana", "mango", "berry", "pinapple", "melon", "cherry", "kiwi" ]
# print(thislist)
# print(len(thislist))
# print(type(thislist))

# 02 - Accessing Items on a List
# print(thislist[1])
# print(thislist[2:5])
# check if an item exists
# if "apple" in thislist:
#     print("Item is present")
# else:
#     print("Item not found")

# 03 - Changing Items on a List
# thislist[1] = "blackcurrant"
# print(thislist)
# thislist.insert(0, "Orange")
# print(thislist)
# thislist[0] = "Orange"
# print(thislist[0])

# 04 - Adding Items on a List
# thislist.append("Orange")
# thislist.insert(0, "Orange")
# newlist = ["orange", "cabbage"]
# thislist.extend(newlist)

# 05 - Removing Items on a list
# thislist.remove("banana")
# thislist.pop(0)
# thislist.pop()
# del thislist[0]
# del thislist 
# thislist.clear()

# 06 - loop list in python
# loop using for loop
# for x in thislist:
#     print(x)
# Loop using range() and len() with a specified index number of an item
# for i in range(len(thislist)):
#     print(thislist[i])

# Loop using for loop
# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i = i + 1

# List Comprehension
# [print(x) for x in thislist]

# 07 - List Comprehension in Python
# list comprehension using for loop
# newlist = []
# for x in thislist:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)

# using list comprehension (one line of code)
# [expression for item in iretable codition is true]
# newlist = [x if x != "banana" else "Flivian" for x in thislist if "a" in x]
# print(newlist)

# 08 - Sort List in python
# thislist.sort(key=str.lower, reverse=True)
# thislist.reverse()
# print(thislist)

# 09 - Copy List in python
# thislist.pop(-1)
# newlist = thislist.copy()
# anotherlist = list(thislist) #using the list method
# morelist = thislist[:]  #using the slice operator 
# print(newlist)
# print(anotherlist)
# print(morelist)

# 10 - Join Lists
# list2 = [20, 30]
# list3 = thislist + list2 #using the + operator
# using the for loop
# for x in list2:
#     thislist.append(x)
# using the extend method
# thislist.extend(list2)
# print(thislist)

"""
Coding Challege on List
1. Create a list called colors with the values "red", "green", "blue"
2. Print the first item in the list
3. Change the second item to "yellow"
4. Add "purple" to the end of the list using append()
5. Remove "red" from the list using remove()
6. Print the list
"""
# Implementation
colors = ["red", "green", "blue"]
print(colors[1])
colors[1] = "yellow"
colors.append("purple")
colors.remove("red")
# expected output ["yellow", "blue", "purple"]
print(colors)






