# Concept Learnt on advanced function 

# Exercise 1. Default paramenters
# Create a function called calculate_price(price, tax=0.16) that returns the price including tax.
def calculate_price(price, tax=0.16):
    return round(price * (1 + tax), 2)

# print(calculate_price(100))
# print(calculate_price(200, 0.2))

# Exercise 2. *args
def calculate_average(*marks):
    if not marks:
        return "No marks provided"
    return sum(marks)/len(marks)
    
# print(calculate_average(20, 30))
# print(calculate_average())
