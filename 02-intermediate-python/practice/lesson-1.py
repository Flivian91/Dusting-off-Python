# Lesson 1 -- advanced function 

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

# Exercise 3. **kwargs
def student_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

# student_profile(
#     name="Alex",
#     age=20,
#     course="Cybersecurity",
#     country="Kenya"
# )

# Exercise 4. Lambda functions
larger_number = lambda a, b: max(a, b)
# print(larger_number(4, 8))
# print(larger_number(5, 5))

# Exercise 5 — Combining concepts
def create_report(title, *scores, **details):
    # display title
    print(f"Report: {title}")
    if not scores:
        print("No scores provided")
    else:
        # calculate and display average score
        average_score = round(sum(scores) / len(scores), 1)
        print(f"Average Score: {average_score}\n")
    # additional details
    print("Additional Details:")
    for key, value in details.items():
        print(f"{key}: {value}")
create_report(
    "Python Assessment",
    80, 93, 72,
    student="Alex",
    course="Cybersecurity",
    level="Beginner"
)