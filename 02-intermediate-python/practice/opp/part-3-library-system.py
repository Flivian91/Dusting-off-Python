class Book:
    # class attributes 
    library_name = "Tech Digital Library"
    late_fee_per_day = 20
    total_books = 0
    borrowing_period = 14
    
    def __init__(self, book_id, title, author, category, total_copies):
        if total_copies < 0:
            raise ValueError("Book copies cannot be negative")
        # Initialize Instance attributes
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.total_copies = total_copies
        self.available_copies = total_copies
        
        # Increment total books
        Book.total_books += 1
        
        # Method Instances
    def display_info(self):
        """Display formated Book details"""
        return (
            f"Book ID: {self.book_id}\n"
            f"Book Title: {self.title}\n"
            f"Book Author: {self.author}\n"
            f"Book Category: {self.category}\n"
            f"Total Available Copies: {self.available_copies}\n"
        )
        
    def is_available(self):
        """Checks if a book is available"""
        return self.available_copies > 0
    
    def borrow_book(self, quantity = 1):
        """Reduces the available books by quantity of books to be borrowed"""
        if quantity < 0:
            raise ValueError("Number of book borrowed cannot be negative")
        if self.available_copies < 0:
            raise ValueError("Not enough available copies.")
        if quantity > self.available_copies:
            raise ValueError("Number of books to be borrowed is more than available books in library")
        # reduce available books
        self.available_copies -= quantity
    
    def return_book(self, quantity = 1):
        """Increase the available books by quantity of books to be borrowed"""
        if self.total_copies == self.available_copies:
            return ValueError("No borrowed copies to return.")
        if quantity < 0:
            raise ValueError("Number of book borrowed cannot be negative")
        if quantity > self.available_copies:
            raise ValueError("Number of books to be borrowed is more than available books in library")
        # reduce available books
        self.available_copies += quantity
    
    def calculate_late_fee(self, days_borrowed):
        """Calculates overdue dates leading to late fees"""
        if days_borrowed < 0:
            raise ValueError("Days borrowed cannot be negative")
        overdue_days = days_borrowed - Book.borrowing_period
        if overdue_days < 0:
            return 0
        else:
            return overdue_days * Book.late_fee_per_day
    
    def get_borrowed_copies(self):
        """Returns the number of borrowed copies"""
        return self.total_copies - self.available_copies
    
    def add_copies(self, quantity=1):
        """Increases both total and availble copies in the library"""
        if quantity < 0:
            raise ValueError("Number of book borrowed cannot be negative")
        self.available_copies += quantity
        self.total_copies += quantity


# CREATE A BOOK OBJECT
books = [
    Book(101, "Python Programming", "Alex", "Programming", 5),
    Book(102, "Database Fundamentals", "Mary", "Database", 3),
    Book(103, "Web Development", "John", "Programming", 4),
    Book(104, "Computer Networks", "David", "Networking", 2),
    Book(105, "Linux Essentials", "Sarah", "Operating Systems", 6)
]

# Borrowing Operation
books[0].borrow_book(3)
books[1].borrow_book(3)
books[2].borrow_book(1)
books[3].borrow_book(2)
books[4].borrow_book(2)

# Advance data processing
# Check available books
available_books = list(filter(lambda book: book.total_copies, books))

# Books Names
book_names = [book.title for book in books]
print(f"Book Names: {book_names}")

# Map IDs to available copies
available_books_lookup = {book.book_id: book.available_copies for book in books}
print(f"Availble books Formated: {available_books_lookup}")

# get all categories
categories = {book.category for book in books}
print(f"Book Categories: {categories}")

# Total available copies
total_available_copies = sum(book.available_copies for book in books)
print(f"Total available copies: {total_available_copies}")

# Total borrowed copies
total_borrowed_copies = sum(book.get_borrowed_copies() for book in available_books)
print(f"Total borrowed copies: {total_borrowed_copies}")

# Sort available copy in descending order
sorted_books = list(book.title for book in sorted(available_books, key=lambda book: book.available_copies, reverse=True))
print(f"Sorted Book Titles: {sorted_books}")

# apply late fees (Very difficult)
late_fees = list(map(lambda book: book.calculate_late_fee(x), books) for x in [7, 14, 20, 30])
print(late_fees)

# APPLICATION FUNCTIONS
# Restock with category
def restock_category(books, category, quantity=1):
    if quantity < 0: 
        raise ValueError("Negative value not accepted")
    
    for book in books:
        if book.category == category:
            book.add_copies(quantity)
            
# Calculate total inventory
def calculate_total_inventory(books):
    return sum(book.total_copies for book in books)

# Search book
def search_books(books, keyword):
    for book in books:
        if book.title.split(keyword.lower()):
            return book.title
        
# Test Restock function
restock_category(books, "Programming", 3)

# test Search function
results = search_books(books, "python")
print(results)

# Test Shared Class attributes
# Change late fee rate 
Book.late_fee_per_day = 30
print(books[0].calculate_late_fee(20))

# Change the borroeing period
Book.borrowing_period = 21
print(books[0].calculate_late_fee(20))

# Invalid book creation
try:
    invalid_book = Book(106, "Python Programming", "Alex", "Programming", -2)
except ValueError as error:
    print(f"Book creation error: {error}")
    
# BONUS Challege
def generate_library_report(books):
    pass