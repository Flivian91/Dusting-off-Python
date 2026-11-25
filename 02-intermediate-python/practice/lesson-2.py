# Lesson 2 -- Comprehensions and advanced collections

# Exercise 1. List comprehension
# Method-1
prices = [100, 200, 300, 400, 500]
discounted_prices = [price * (1- 0.1) for price in prices]
# print(discounted_prices)
# Method -2
discounted_prices_older = []
for price in prices:
    discounted_prices_older.append(price * (1 - 0.1))
# print(discounted_prices_older)

# Exercise 2 — Filtering product records
# Method - 1
products = [
    {"name": "Laptop", "price": 800, "stock": 5},
    {"name": "Mouse", "price": 20, "stock": 0},
    {"name": "Keyboard", "price": 50, "stock": 12},
    {"name": "Monitor", "price": 300, "stock": 3},
    {"name": "Headphones", "price": 100, "stock": 0}
]
available_products = [product for product in products if product['stock'] > 0]
# print(available_products)
# Method - 2
available_products_older = []
for product in products:
    if product["stock"] > 0:
        available_products_older.append(product)
# print(available_products_older)

# Exercise 3 - Conditional expression
# Method - 1
students = [
    {"name": "Alex", "score": 85},
    {"name": "John", "score": 42},
    {"name": "Mary", "score": 67},
    {"name": "David", "score": 35},
    {"name": "Sarah", "score": 90}
]
student_results = ["Pass" if student["score"] >= 50 else "Fail" for student in students]
# print(student_results)
# Method - 2
student_results_older = []
for student in students:
    student_results_older.append("Pass" if student["score"] >= 50 else "Fail")
# print(student_results_older)
# Exercise 4 — Dictionary comprehensions
# Method - 1
users = [
    {"id": 101, "name": "Alex"},
    {"id": 102, "name": "John"},
    {"id": 103, "name": "Mary"},
    {"id": 104, "name": "David"}
]
user_lookup = {user['id']: user["name"] for user in users}
# print(user_lookup)
# Method - 2
user_lookup_older = {}
for user in users:
    # use any of 2 formats below
    user_lookup_older.update({user["id"]: user["name"]})
    # user_lookup_older[user["id"]] = user["name"]
# print(user_lookup_older)
# Backend connection: This pattern is useful when building lookup tables, mapping database records by ID, and transforming API responses.
# 1. Raw data from two separate API endpoints or database tables
customers = [
    {"user_id": "USR-101", "name": "Wanjiku Mwangi", "phone": "+254712345678"},
    {"user_id": "USR-102", "name": "Otieno Odhiambo", "phone": "+254723456789"},
    {"user_id": "USR-103", "name": "Fatuma Hassan", "phone": "+254734567890"},
    {"user_id": "USR-104"},
]

transactions = [
    {"tx_id": "TXN-9001", "user_id": "USR-102", "amount_kes": 1500},
    {"tx_id": "TXN-9002", "user_id": "USR-101", "amount_kes": 450},
    {"tx_id": "TXN-9003", "user_id": "USR-999", "amount_kes": 2200}, # Unknown user
]

# 2. Build the lookup table (O(n) time - runs only once)
customer_lookup = {c["user_id"]: c for c in customers}


# 3. Transform/enrich transactions using instant O(1) lookups
enriched_receipts = []

for tx in transactions:
    # .get() safely returns a fallback dictionary if the user_id isn't found
    customer = customer_lookup.get(tx["user_id"], {"name": "Unknown Customer", "phone": "N/A"})
    
    enriched_receipts.append({
        "receipt_no": tx["tx_id"],
        "customer_name": customer["name"],
        "phone": customer["phone"],
        "amount": f"KES {tx['amount_kes']:,}"
    })

# Exercise 5 — Set comprehensions
emails = [
    "alex@gmail.com",
    "john@yahoo.com",
    "mary@gmail.com",
    "david@outlook.com",
    "sarah@yahoo.com",
    "peter@gmail.com"
]
email_domains = {domain.split("@")[1] for domain in emails}
# print(email_domains)
# Backend connection: This is useful for analysing user registration data, grouping users by email provider, and processing records.

# Exercise 6 — Nested list comprehensions
# method_1
warehouse_stock = [
    [10, 20, 30],
    [15, 25, 35],
    [5, 10, 15]
]
all_stocks = [item for stock in warehouse_stock for item in stock]
# print(all_stocks)
# methond_2
all_stocks_older = []
for stock in warehouse_stock:
    for item in stock:
        all_stocks_older.append(item)
# print(all_stocks_older)

# Python Transformation tools (map(), filter() and zip())
#01 - map() - applies a function to every item in an iterable
# Example
prices = [100, 200, 300, 400]
def add_tax(price):
    return price * 1.16

taxed_prices = list(map(lambda price : price * 1.16, prices))
# print(taxed_prices)

# Exercise 7 - map()
prices = [100, 200, 300, 400, 500]
def discount_price(price):
    return price * (1 - 0.15)
discounted_prices = list(map(lambda price: price * (1 - 0.15), prices))
# print(discounted_prices)

# 02: filter() - Selects items from an iterable based on a condition.
# Example
prices = [50, 120, 250, 80, 400]
def check_expensive_products(price):
    if(price > 100):
        return price
expensive_products = list(filter(lambda price: price > 100, prices))
# print(expensive_products)

# Exercise 8 - Filter()
users = [
    {"name": "Alex", "age": 17},
    {"name": "John", "age": 24},
    {"name": "Mary", "age": 19},
    {"name": "David", "age": 15},
    {"name": "Sarah", "age": 28}
]
adults = list(filter(lambda user: user["age"] >= 18, users))
# print(adults)

# 03: zip() - combines corresponding items from two or more iterables
names = ["Alex", "John", "Mary"]
ages = [20, 25, 19]

users = list(zip(names, ages))
# print(users)

# Exercise 8 - zip()
product_names = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [800, 20, 50, 300]

products = dict(zip(product_names, prices))
print(products)