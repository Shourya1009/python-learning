"""
Introduction to Object-Oriented Programming (OOP)
-------------------------------------------------
Object-Oriented Programming (OOP) is a programming paradigm that organizes
code into **objects** — reusable components that contain **data** (attributes)
and **behavior** (methods).

Benefits of OOP:
- Modularity: Code is organized into classes and objects.
- Reusability: Code can be reused using inheritance.
- Scalability: Easier to expand and maintain.
- Abstraction: Hides complex implementation details.
- Encapsulation: Bundles data and methods together, restricting direct access.

-------------------------------------------------
Key Concepts of OOP
-------------------------------------------------

1. Class:
   - A blueprint for creating objects.
   Example:
       class Car:
           pass

2. Object:
   - An instance of a class.
   Example:
       my_car = Car()

3. Encapsulation:
   - Hiding the internal state and requiring all interaction
     to occur through methods.

4. Inheritance:
   - A class can inherit attributes and methods from another class.
   Example:
       class ElectricCar(Car):
           pass

5. Polymorphism:
   - The ability to use a single interface for different data types.
   - Example: Methods with the same name behaving differently.

6. Abstraction:
   - Hiding complex implementation details and showing only the essential features.

-------------------------------------------------
Example Code
-------------------------------------------------
"""

# Defining a class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} is starting...")

# Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    # Method overriding (Polymorphism)
    def start(self):
        print(f"{self.brand} {self.model} is starting silently with a {self.battery_capacity} kWh battery.")

# Creating objects
car1 = Car("Toyota", "Corolla")
car2 = ElectricCar("Tesla", "Model S", 100)

# Using methods
car1.start()
car2.start()
