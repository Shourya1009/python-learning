"""
Method Overriding and Operator Overloading in Python
----------------------------------------------------

1. Method Overriding:
   - Happens when a child class redefines a method of the parent class.
   - The child class provides its own implementation.
   - Requires inheritance.

2. Operator Overloading:
   - Python uses special (dunder) methods to define operator behavior.
   - Allows operators to work differently for custom objects.
   - Example: '+' can add numbers, join strings, or add objects.

-------------------------------------------------
Example: Method Overriding
-------------------------------------------------
"""

# Parent class
class Animal:
    def sound(self):
        print("Animals make different sounds.")

# Child class 1
class Dog(Animal):
    def sound(self):  # Overriding
        print("Dog says: Bark!")

# Child class 2
class Cat(Animal):
    def sound(self):  # Overriding
        print("Cat says: Meow!")

# Demonstration
print("Method Overriding Example:\n")

animals = [Animal(), Dog(), Cat()]

for obj in animals:
    obj.sound()

"""
Output:
Animals make different sounds.
Dog says: Bark!
Cat says: Meow!
"""

# ------------------------------------------------
# Example: Operator Overloading
# ------------------------------------------------

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading '+' operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # String representation
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    # Optional: equality check
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# Demonstration
print("\nOperator Overloading Example:\n")

p1 = Point(2, 3)
p2 = Point(4, 5)

p3 = p1 + p2   # Calls __add__

print("p1 =", p1)
print("p2 =", p2)
print("p1 + p2 =", p3)

# Extra check
print("Are p1 and p2 equal?", p1 == p2)

"""
Output:
Operator Overloading Example:

p1 = Point(2, 3)
p2 = Point(4, 5)
p1 + p2 = Point(6, 8)
Are p1 and p2 equal? False
"""