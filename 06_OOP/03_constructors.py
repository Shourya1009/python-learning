"""
Constructors in Python
----------------------

A constructor in Python is a special method used to initialize objects
when they are created from a class.

The most commonly used constructor is:
    __init__(self, ...)

Key Points:
- It is automatically called when an object is created.
- The first parameter is always `self`, which refers to the current object.
- You can pass additional parameters to set initial values for attributes.

-------------------------------------------------
Types of Constructors in Python
-------------------------------------------------

1. Default Constructor:
   - Takes only `self` as a parameter.
   - Used when no initialization is needed.

2. Parameterized Constructor:
   - Accepts additional arguments to initialize attributes.

-------------------------------------------------
Example Code
-------------------------------------------------
"""

# 1. Default Constructor
class DefaultExample:
    def __init__(self):
        print("This is a default constructor.")

obj1 = DefaultExample()  # Automatically calls __init__


# 2. Parameterized Constructor
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"Car Created: {self.brand} {self.model}")

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

car1.display()
car2.display()

"""
Output:
This is a default constructor.
Car Created: Toyota Corolla
Car Created: Honda Civic
Brand: Toyota, Model: Corolla
Brand: Honda, Model: Civic
"""
