# Task - 1 and 2- create a class and implement methods
class Product:
    def __init__(self, product_id, name, price, stock, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
        
    def display_info(self):
        return f"Product ID: {self.product_id}\nProduct Name: {self.name}\nPrice:Ksh. {self.price}\nStock: {self.stock}\nCategory: {self.category}\n"
    
    def is_available(self):
        return self.stock > 0
    
    def calculate_inventory_value(self):
        return self.price * self.stock
    
    def calculate_discounted_price(self, discount=10):
        return self.price * (1 - discount/100)
    
products = [
    Product(101, "Laptop", 800, 5, "Electronics"),
    Product(102, "Mouse", 20, 0, "Accessories"),
    Product(103, "Keyboard", 50, 12, "Accessories"),
    Product(104, "Monitor", 300, 3, "Electronics"),
    Product(105, "Headphones", 100, 0, "Accessories")
]

# Get the available products
available_products = list(filter(lambda product: product.is_available(), products))
# Show available products with names
product_names = [product.name for product in available_products]
# print(product_names)
# Show every product with there names
product_lookup = {product.product_id: product.name for product in available_products}
# print(product_lookup)
total_inventory_value = sum(product.calculate_inventory_value() for product in products)
# print(total_inventory_value)
categories = {product.category for product in products}
# print(categories)
discounted_price = list(map(lambda product: product.calculate_discounted_price(15), products))
# print(discounted_price)
# Bonus
sorted_names = [product.name for product in sorted(available_products, key=lambda product: product.price, reverse=True)]
print(sorted_names)
