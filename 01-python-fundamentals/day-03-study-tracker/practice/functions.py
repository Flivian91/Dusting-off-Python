# Function is a block of code that only run when called
# functions are defined using the def keyword, followed by name and round brackets
# def my_function():
#     print("This is a function") 
# my_function() #calling or invoking the function
# my_function()

# 01 - pyhton function arguments
# default parameters
# def my_name(fname, lname="Mwirigi"): #fname is a parameter
#     print(fname + " " + lname)
    
# my_name("Flivian", "Kimani") # what is passed in the function calling is called an argument
# my_name("kelvin")

# keywords arguments
# def my_pet(animal, name):
#     print(animal.capitalize() + " is my favourite pet is called " + name.capitalize())

# my_pet(name="flivo", animal="Cat") #the order doesnot matter bcz of keyword argument

# 02 -Python *args and **kwargs
# def my_child(*kids):
#     print("This is my youngest kid " + kids[0])
# my_child("Flivian", "Peter", "Amos")
# Example
# a)Create a function that calculate the sum of any numbers
def sum_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
# print(sum_numbers(1,2,3,4))
# print(sum_numbers(30, 40 ,40))
# b) Create a function that check for the maximum number
def max_number(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
# print(max_number(1,2,3,4,5))
# print(max_number(40,23,58,39))
# c) Create a function that check for the minimum number
def min_number(*numbers):
    if len(numbers) == 0:
        return None
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num
# print(min_number(20, 30, 40))
# print(min_number(38,48,29,49))

# Combining positional(*args) and keyword arguments(**kwargs)
# Order must be followed 1. regular argument, 2. *args, 3. **kwargs
def combing_args(normal_args, *args, **kwargs):
    print("This is a regular Arguments:" , normal_args) #returns a str
    print("This is Positional (*args):" , args) #returns a tuple
    print("This is Keywords (**kwargs):" , kwargs) #returns a dict

# combing_args("Flivian", "Amons", "Peter", name="Omondi", age=22)

# 03 -Python Scope
# The LEGB Rule in python
x = 'Global Variable'
def outer_function():
    x = "Enclosing Variable"
    def inner_function():
        x = "Local Variable"
        print(x)
    inner_function()
    print(x)
# outer_function()
# print(x)

"""
Coding challenge
1. Create a function called greet
2. Add a parameter called name to the function
3. Inside the function, print "Hello, " followed by the name parameter
4. Call the function with the argument "Emil"
"""
# Implementation
def greet(name):
    print("Hello, " + name)

# calling
greet("Emil")