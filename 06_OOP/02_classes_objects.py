"""
Classes and Objects in Python
-----------------------------

1. Class:
   - A blueprint used to create objects.
   - It defines attributes (data) and methods (functions).

2. Object:
   - An instance of a class.
   - Each object has its own data but shares the class behavior.

Why use Classes & Objects?
- Organize code into logical structures
- Improve code reusability
- Represent real-world entities in programs

-------------------------------------------------
Basic Example
-------------------------------------------------
"""

# Defining a class
class Car:
    # Constructor → runs automatically when object is created
    def __init__(self, brand, model):
        self.brand = brand      # Instance attribute
        self.model = model      # Instance attribute

    # Method → defines behavior of the object
    def start(self):
        print(f"{self.brand} {self.model} is starting...")

# Creating objects (instances of Car)
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Accessing object attributes
print("Car 1 Brand:", car1.brand)
print("Car 2 Model:", car2.model)

# Calling object methods
car1.start()
car2.start()

"""
Expected Output:
Car 1 Brand: Toyota
Car 2 Model: Civic
Toyota Corolla is starting...
Honda Civic is starting...
"""