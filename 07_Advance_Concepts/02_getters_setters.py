"""
Getters and Setters in Python
-----------------------------

In Object-Oriented Programming, getters and setters are used to access and modify
the attributes of a class.

1. Getter:
   - A method that allows us to access (get) the value of a private attribute.

2. Setter:
   - A method that allows us to modify (set) the value of a private attribute.

Why use Getters and Setters?
- Encapsulation: Restrict direct access to private attributes.
- Validation: Ensure only valid values are assigned to attributes.
- Flexibility: Implementation details can change without affecting external code.

In Python, the `@property` decorator is commonly used to create getters and setters.
"""

# Example: Using Getter and Setter

class Person:
    def __init__(self, name, age):
        self._name = name      # Protected attribute (convention: single underscore)
        self._age = age        # Protected attribute

    # Getter for age
    @property
    def age(self):
        return self._age

    # Setter for age
    @age.setter
    def age(self, value):
        if value < 0:
            print("Age cannot be negative!")
        else:
            self._age = value

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, value):
        if not value.strip():
            print("Name cannot be empty!")
        else:
            self._name = value

# Demonstration
p = Person("Shourya", 23)

# Using getters
print("Name:", p.name)
print("Age:", p.age)

# Using setters with validation
p.age = 25        # Valid
print("Updated Age:", p.age)

p.age = -5        # Invalid

p.name = "Aman"    # Valid
print("Updated Name:", p.name)

p.name = "   "    # Invalid
