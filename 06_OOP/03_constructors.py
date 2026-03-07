"""
Constructors in Python
----------------------

A constructor in Python is a special method that is automatically
called when an object of a class is created.

The most commonly used constructor is:
    __init__(self, ...)

Key Points:
- It runs automatically when an object is created.
- The first parameter is always `self`, which refers to the current object.
- Additional parameters can be used to initialize object attributes.

-------------------------------------------------
Types of Constructors in Python
-------------------------------------------------

1. Default Constructor
   - Takes only `self` as a parameter.
   - Used when no initial values are required.

2. Parameterized Constructor
   - Takes extra parameters to initialize attributes.
"""

# 1. Default Constructor Example
class DefaultExample:
    def __init__(self):
        self.message = "Object initialized using default constructor."
        print(self.message)

# Creating object (constructor runs automatically)
obj1 = DefaultExample()


# 2. Parameterized Constructor Example
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"Car object created -> {self.brand} {self.model}")

    def display_details(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")
        print("----------------------")

# Creating objects with parameters
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Calling method to display details
car1.display_details()
car2.display_details()


"""
Expected Output:

Object initialized using default constructor.
Car object created -> Toyota Corolla
Car object created -> Honda Civic
Car Brand: Toyota
Car Model: Corolla
----------------------
Car Brand: Honda
Car Model: Civic
----------------------
"""