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
print(available_products)