# dictionsries in python
# -they are collection which is orderd*, changeable and does not allow duplicates values
# -they are written in curly brackets and havr key and values pairs

thisdict = {
    "name": "flivian",
    "gender": "male",
    "country": "kenya",
    "age": 22,
    "health_records":{
        "diabates": False,
        "hiv": False,
        "pressure": False,
    }
}
# print(thisdict["name"])
# print(len(thisdict))
# print(type(thisdict))
# person = dict(name = "kelvin", age = 20, country = "uganda", disable = False)
# print(person["name"])

# 01 - Accessing dictionary items
# print(thisdict["country"])
# print(thisdict.get("age"))
# print(thisdict.keys())
# print(thisdict.values())
# print(thisdict.items())

# 02 - Updating disctionary items
# thisdict["name"] = "Mwirigi"
# thisdict.update({"name": "Mwirigi"})
# print(thisdict)

# 03 - Adding Dictionary items
# thisdict["dob"] = "20/03/2026"
# thisdict.update({"color": "black"})
# print(thisdict)

# 04 -Removing dictionary items
# thisdict.pop("name")
# thisdict.popitem() #removers the last item in the dictionary
# del thisdict["country"]
# del thisdict # this deletes the entire dictionary completely
# thisdict.clear()
# print(thisdict)

# 05 - loop Through a Dictionary
# -Using for loop
# return the keys only
# for x in thisdict:
#     print(x)
# returns the values only
# for x in thisdict:
#     print(thisdict[x])
# To loop through both keys and values
# for i,j in thisdict.items():
#     print(f"{i}: {j}")

# 06 - Nested Dictionary
# print(thisdict["health_records"]["pressure"]) #accessing the nested dictionary
# for x, obj in thisdict.items():
#     print(x)
"""
Coding Challenge
1. Create a dictionary called car with the keys "brand", "model", "year" and values "Ford", "Mustang", 2024
2. Print the value of the "model" key
3. Add a new key "color" with the value "red"
4. Remove the "brand" key using pop()
5. Print the dictionary
"""
# Implementation
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2024
}
print(car["model"])
car["color"] = "red"
car.pop("brand")
print(car)