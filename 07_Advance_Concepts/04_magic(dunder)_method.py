"""
Magic (Dunder) Methods in Python
--------------------------------

In Python, *magic methods* (also called *dunder methods* because they have
double underscores before and after their names) are special methods
that give classes extra functionality.

They let you define how objects of your class should behave with built-in
Python operations (like printing, addition, comparisons, iteration, etc.).

Examples:
- __init__  → Object constructor
- __str__   → String representation
- __len__   → Defines behavior for len()
- __add__   → Defines behavior for +
- __eq__    → Defines behavior for ==
- __getitem__ → Enables indexing (obj[i])
- __iter__  → Makes object iterable

-------------------------------------------------
Example Code
-------------------------------------------------
"""

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # __str__ → readable string representation
    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"

    # __len__ → called by len()
    def __len__(self):
        return self.pages

    # __add__ → adding two Book objects (combine pages)
    def __add__(self, other):
        return self.pages + other.pages

    # __eq__ → equality check
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

# Demonstration
book1 = Book("Python Basics", "Shourya", 250)
book2 = Book("Advanced Python", "Aman", 300)
book3 = Book("Python Basics", "Shourya", 250)

# __str__
print(book1)  

# __len__
print("Pages in book1:", len(book1))

# __add__
print("Total pages (book1 + book2):", book1 + book2)

# __eq__
print("book1 == book2 ?", book1 == book2)
print("book1 == book3 ?", book1 == book3)