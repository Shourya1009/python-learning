"""
Classes and Objects in Python
-----------------------------

1. Class:
   - A blueprint for creating objects.
   - Defines attributes (data) and methods (functions) that the objects will have.

2. Object:
   - An instance of a class.
   - Has its own data but shares the structure and behavior defined by the class.

Why use Classes & Objects?
- Organize code into logical units.
- Reuse code easily.
- Model real-world entities.

-------------------------------------------------
Basic Example
-------------------------------------------------

"""

# Defining a class
class Car:
    # Constructor (initializes object attributes)
    def __init__(self, brand, model):
        self.brand = brand  # Attribute
        self.model = model  # Attribute

    # Method (behavior)
    def start(self):
        print(f"{self.brand} {self.model} is starting...")

# Creating objects (instances of Car)
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Accessing attributes
print("Car 1 Brand:", car1.model)
print("Car 2 Model:", car2.model)

# Calling methods
car1.start()
car2.start()

"""
Output:
Car 1 Brand: Toyota
Car 2 Model: Civic
Toyota Corolla is starting...
Honda Civic is starting...
"""
