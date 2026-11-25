#Part 1 -- Classes and Objects

# 1. What is OOP?
# OPP -is a programming approach that organizes software around objects that contains both data and behavior
# One class can create multiple objects with different data but share behaviour.
# A class is a blueprint for creating object.
# An object is an instance of that class 
# By convention, Python class name uses PascalCase while function and variable uses snake_case
# self -refers to the current instance of the class
# Attributes represents an object`s data while methods represents its behaviour
class Product:
    # Class attributes
    currency = "KES"
    tax_rate = 0.16
    total_products = 0
    def __init__(self, name, price, stock): #automatically runs when the object is created
        # Instance attributes and they belong to individual object
        self.name = name
        self.price = price
        self.stock = stock
        # Increments the total products when a new object is created
        Product.total_products += 1
    def display_info(self):
        return f"{self.name} | Price: {self.price} | Stock: {self.stock}"
    def calculate_value(self):
        return self.price * self.stock
    def is_available(self):
        return self.stock > 0

# creating object
p1 = Product("Laptop", 800, 5)
p2 = Product("Mouse", 20, 12)
p3 = Product("Mouse", 20, 12)
# storing object in a list
products = [
    Product("Laptop", 800, 5),
    Product("Mouse", 20, 0),
    Product("Keyboard", 50, 12),
    Product("Monitor", 300, 3)
]
# Use list comprehension to show availability
available_products = [
    product for product in products if product.is_available()
]
# print(available_products)

product_names = list(map(lambda product: product.name, products))
print(product_names)

product_prices = {product.name: product.price for product in products}
# print(product_prices)

total_value = [product.calculate_value() for product in products]
# print(sum(total_value))

# Exercise 1 — E-commerce Product System
# Implemented on day-01 of OPP

# PART- 2: Instance and class attributes
# Accessing class instance
# print(p1.currency)
# Modifying class instance
# Product.currency = "USD"
# # print(p1.currency)
# print(p2.currency)

# Attribute shadowing
# p1.currency = "EUR"
# print(p1.currency) #has changed its object only
# print(p2.currency)
# print(Product.currency)
# 
# Tracking objects using class attributes
# Product.total_products += 1 # Increments counter
# print(Product.total_products)

# Avoid using class attributes with list or dictionaries