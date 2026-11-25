# Lesson 2 -- Comprehensions and advanced collections

# Exercise 1. List comprehension
prices = [100, 200, 300, 400, 500]
discounted_prices = [x * (1- 0.1) for x in prices]
# print(discounted_prices)

# Exercise 2 — Filtering product records
products = [
    {"name": "Laptop", "price": 800, "stock": 5},
    {"name": "Mouse", "price": 20, "stock": 0},
    {"name": "Keyboard", "price": 50, "stock": 12},
    {"name": "Monitor", "price": 300, "stock": 3},
    {"name": "Headphones", "price": 100, "stock": 0}
]
available_products = [product for product in products if product['stock'] > 0]
# print(available_products)

# Exercise 3 - Conditional expression
students = [
    {"name": "Alex", "score": 85},
    {"name": "John", "score": 42},
    {"name": "Mary", "score": 67},
    {"name": "David", "score": 35},
    {"name": "Sarah", "score": 90}
]
student_results = ["Pass" if score["score"] >= 50 else "Fail" for score in students]
# print(student_results)

# Exercise 4 — Dictionary comprehensions
users = [
    {"id": 101, "name": "Alex"},
    {"id": 102, "name": "John"},
    {"id": 103, "name": "Mary"},
    {"id": 104, "name": "David"}
]
user_lookup = {user['id']: user["name"] for user in users}
# print(user_lookup)
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
print(all_stocks)
# methond_2
all_stocks_older = []
for stock in warehouse_stock:
    for item in stock:
        all_stocks_older.append(item)
print(all_stocks_older)