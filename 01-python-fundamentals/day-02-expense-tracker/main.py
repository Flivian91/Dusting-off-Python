# Expense tracker is an application that allow users to record, view, search and calculate there personal expenses
expenses = [
    {
        "name": "Lunch",
        "amount": 250,
        "category": "Food"
    },
    {
        "name": "Lunch",
        "amount": 400,
        "category": "Food"
    },
    {
        "name": "Party",
        "amount": 600,
        "category": "Travel"
    },
    {
        "name": "Transport",
        "amount": 100,
        "category": "Travel"
    }
]

# Introduction to the application
# Introduction Function
def user_welcome():
    print("==========WELCOME TO PERSONAL EXPENSE TRACKER==========")
    menuitems = ["Add Expense", "View all Expenses", "View Total Expenses", "View Expense by Category", "View Expense by Name", "Exit"]
    i = 0
    for x in menuitems:
        print(f"{i + 1}. {x}")
        i+=1
    try:
        user_option = int(input("Choose an option: "))
        if user_option < 1 or user_option > 6:
            print("Please enter valid value form 1 to 6")
        return user_option
    except ValueError:
        print("Please enter a whole number from 1 to 6")
        return
        
# option = user_welcome()

# Option 1: Add Expense
def add_expense():
    print("======= ADD EXPENSE ======= \n")
    expense_name = input("Enter expense name: ")
    if not expense_name.strip():
        print("Expense name cannot be empty")
        return
    try:
        expense_amount = int(input("Enter expense amount: "))
        if expense_amount < 0 or expense_amount == 0:
            print("Please enter value more than 0")
            return
    except ValueError:
        print("Please enter a whole number")
        return
    expense_category = input("Enter expense category: ")
    if not expense_category.strip():
        print("Expense category cannot be empty")
        return
    
    expenses.append({"name": expense_name, "amount": expense_amount, "category": expense_category})
    
# add_expense()
# Option 2: View all expenses

def view_expense():
    print("======= ALL EXPENSES ======= \n")
    i = 1
    for x in expenses:
        print(f"| {i}. {x['name']} \t | {x['amount']} | {x['category']}\t |")
        i+=1
# view_expense()

# Option 3: Total expense
def total_expense():
    print("======= TOTAL EXPENSES ======= \n")
    total = []
    for x in expenses:
        total.append(x["amount"])
    print(f"Total Expenses: {sum(total)}")
# total_expense()

# Option 4: Search Expense by Category
def search_expense_category():
    print("======= SEARCH EXPENSE BY CATEGORY ======= \n")
    search_query = input("Enter category: ")
    if not search_query.strip():
        print("Please Category cannot be empty")
        return
    found = False
    for x in expenses:
        value = x["category"]
        if search_query.lower() == value.lower():
            print(f"{x['name']} - {x['amount']}")
            found = True
    if not found:
        print("Ooops!! No expense available")
    
# search_expense_category()

# Option 5: Search Expense by name
def search_expense_name():
    print("======= SEARCH EXPENSE BY NAME ======= \n")
    search_query = input("Enter expense name: ")
    if not search_query.strip():
        print("Please expense name cannot be empty")
        return
    found = False
    for x in expenses:
        value = x["name"]
        if search_query.lower() == value.lower():
            print(f"Name: {x['name']} \nAmount:{x['amount']} \nCategory: {x['category']} \n")
            found = True
    
    if not found:
        print("Ooops!! No expense available")
# search_expense_name()
# While loop to keep the program running
while True:
    option = user_welcome()
    if option == 1:
        add_expense()
    elif option == 2:
        view_expense()
    elif option == 3:
        total_expense()
    elif option == 4:
        search_expense_category()
    elif option == 5:
        search_expense_name()
    elif option == 6:
        print("Thank you for visiting Personal Expense Tracker")
        break
        