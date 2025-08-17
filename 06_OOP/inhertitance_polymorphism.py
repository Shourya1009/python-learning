"""
Inheritance and Polymorphism in Python
--------------------------------------

1. Inheritance:
   - Inheritance allows a class (child/derived class) to acquire the
     properties and methods of another class (parent/base class).
   - Promotes reusability and a clear hierarchical structure.

   Types of Inheritance in Python:
   - Single Inheritance: Child inherits from one parent.
   - Multiple Inheritance: Child inherits from more than one parent.
   - Multilevel Inheritance: A class inherits from a child class of another class.
   - Hierarchical Inheritance: Multiple child classes inherit from the same parent.
   - Hybrid Inheritance: Combination of different inheritance types.

2. Polymorphism:
   - Means "many forms".
   - In OOP, it allows the same method name to perform different tasks
     depending on the object that calls it.
   - Achieved through **method overriding** or **method overloading (not directly in Python, but can be simulated with default arguments)**.

-------------------------------------------------
Example Code
-------------------------------------------------
"""

# Parent Class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle is starting...")

# Child Class (Single Inheritance)
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Calling parent constructor
        self.model = model

    # Method Overriding (Polymorphism)
    def start(self):
        print(f"{self.brand} {self.model} is starting with a roar!")

# Another Child Class
class ElectricCar(Vehicle):
    def __init__(self, brand, battery_capacity):
        super().__init__(brand)
        self.battery_capacity = battery_capacity

    # Method Overriding (Polymorphism)
    def start(self):
        print(f"{self.brand} is starting silently with a {self.battery_capacity} kWh battery.")

# Demonstrating Inheritance and Polymorphism
v = Vehicle("Generic")
c = Car("Toyota", "Corolla")
e = ElectricCar("Tesla", 100)

v.start()  # Uses Vehicle's method
c.start()  # Uses Car's overridden method
e.start()  # Uses ElectricCar's overridden method

"""
Output:
Generic vehicle is starting...
Toyota Corolla is starting with a roar!
Tesla is starting silently with a 100 kWh battery.
"""

# ------------------------------------------------
# Example of Polymorphism with a Common Interface
# ------------------------------------------------
vehicles = [Car("Honda", "Civic"), ElectricCar("Nissan", 60), Vehicle("Bike")]

for v in vehicles:
    v.start()   # Same method name, different behavior
