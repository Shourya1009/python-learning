"""
Method Overriding and Operator Overloading in Python
----------------------------------------------------

1. Method Overriding:
   - Occurs when a child class provides a specific implementation
     of a method that is already defined in its parent class.
   - The child class method overrides the parent class method.
   - Achieved through inheritance.

2. Operator Overloading:
   - In Python, operators are implemented using special methods (also called dunder methods).
   - Operator overloading allows the same operator to have different meanings depending on the objects.
   - Example: The '+' operator adds numbers, but can also concatenate strings or be customized for objects.

-------------------------------------------------
Example Code: Method Overriding
-------------------------------------------------
"""

# Parent class
class Animal:
    def sound(self):
        print("This animal makes a sound.")

# Child class overriding the method
class Dog(Animal):
    def sound(self):  # Overriding the parent method
        print("The dog barks.")

class Cat(Animal):
    def sound(self):
        print("The cat meows.")

# Demonstration
a = Animal()
d = Dog()
c = Cat()

a.sound()  # Parent method
d.sound()  # Overridden method
c.sound()  # Overridden method

"""
Output:
This animal makes a sound.
The dog barks.
The cat meows.
"""

# ------------------------------------------------
# Example Code: Operator Overloading
# ------------------------------------------------

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Overloading the str() function for readable output
    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2   # Uses __add__

print("\nOperator Overloading Example:")
print("p1:", p1)
print("p2:", p2)
print("p1 + p2 =", p3)

"""
Output:
Operator Overloading Example:
p1: (2, 3)
p2: (4, 5)
p1 + p2 = (6, 8)
"""
