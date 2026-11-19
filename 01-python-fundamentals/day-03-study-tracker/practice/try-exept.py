# try: #tests the block of code for error
#     x = "i am here"
#     print(x)
# except: #allow you to handle error correctly
#     print("Variable not defined")
# else: #executes when there is no error
#     print("Done")
# finally: #executes always regardless or error or not
#     print("Finally")

# Raise an error
# x = "hello"

# if not type(x) is int:
#     raise TypeError("Only Int allowed")

"""
CODING CHALLENGE
1. Write a try block that tries to print a variable x (which is not defined)
2. Write an except block that prints "An error occurred"
3. Write a finally block that prints "Execution complete"
"""
# Implementation
try:
    print(x)
except:
    print("An error occurred")
finally:
    print("Execution complete")
