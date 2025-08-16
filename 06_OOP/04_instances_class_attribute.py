"""
Instances and Class Attributes in Python
----------------------------------------

In Python, attributes are variables that belong to a class or an object.

1. Instance Attributes:
   - Defined inside the constructor (__init__).
   - Unique to each object (instance).
   - Changing one object’s instance attribute does not affect others.

2. Class Attributes:
   - Shared across all instances of the class.
   - Defined directly inside the class, outside of any method.
   - Changing the class attribute affects all objects (unless overridden by the instance).

-------------------------------------------------
Example Code
-------------------------------------------------
"""

class Car:
    # Class Attribute (shared by all objects)
    wheels = 4

    def __init__(self, brand, model):
        # Instance Attributes (unique to each object)
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Wheels: {Car.wheels}")

# Creating objects (instances)
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Accessing instance attributes
print("Car1 Brand:", car1.brand)
print("Car2 Model:", car2.model)

# Accessing class attribute
print("Car1 Wheels:", car1.wheels)
print("Car2 Wheels:", car2.wheels)

# Modifying class attribute (affects all instances)
Car.wheels = 6
print("\nAfter changing class attribute:")
car1.display()
car2.display()

# Overriding class attribute for one instance
car1.wheels = 8
print("\nAfter overriding wheels for car1 only:")
print("Car1 Wheels:", car1.wheels)  # Instance-specific
print("Car2 Wheels:", car2.wheels)  # Still class attribute

"""
Output:
Car1 Brand: Toyota
Car2 Model: Civic
Car1 Wheels: 4
Car2 Wheels: 4

After changing class attribute:
Brand: Toyota, Model: Corolla, Wheels: 6
Brand: Honda, Model: Civic, Wheels: 6

After overriding wheels for car1 only:
Car1 Wheels: 8
Car2 Wheels: 6
"""
