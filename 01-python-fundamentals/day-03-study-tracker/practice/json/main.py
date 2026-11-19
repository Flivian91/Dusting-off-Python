import json


# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse the json(convert from JSON to Python)
# y = json.loads(x)
# print(x)
# print(y["age"])
# Convert from Python to json
students = [
{
    "name": "Flivian",
    "age": 23,
    "status": "single"
},
{
    "name": "Amos",
    "age": 25,
    "status": "single"
},
{
    "name": "Peter",
    "age": 24,
    "status": "married"
}
]
y = json.dumps(students, indent=3, sort_keys=True)
print(y)