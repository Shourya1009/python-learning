"""
Static Methods and Class Methods in Python
------------------------------------------

In Python, apart from instance methods, we can also define methods that
belong to the class itself rather than to individual objects.

1. Instance Method (default):
   - The most common type of method.
   - Takes `self` as the first argument.
   - Can access and modify instance attributes.

2. Class Method:
   - Defined using the `@classmethod` decorator.
   - Takes `cls` (class) as the first argument.
   - Can access and modify **class attributes**, but not instance attributes.
   - Useful for creating factory methods.

3. Static Method:
   - Defined using the `@staticmethod` decorator.
   - Does not take `self` or `cls` as the first argument.
   - Behaves like a normal function but belongs to the class’s namespace.
   - Cannot modify class or instance attributes directly.
   - Used for utility/helper functions.

-------------------------------------------------
Example Code
-------------------------------------------------
"""

class Student:
    school_name = "ABC School"  # Class Attribute

    def __init__(self, name, age):
        self.name = name      # Instance Attribute
        self.age = age

    # Instance Method
    def display(self):
        print(f"Student Name: {self.name}, Age: {self.age}, School: {Student.school_name}")

    # Class Method
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    # Static Method
    @staticmethod
    def is_adult(age):
        return age >= 18


# Demonstration
s1 = Student("Shourya", 17)
s2 = Student("Anuj", 20)

# Instance Method
s1.display()
s2.display()

# Class Method (changes class attribute for all instances)
Student.change_school("XYZ School")
s1.display()
s2.display()

# Static Method (works like a utility function)
print("\nIs 17 adult?", Student.is_adult(17))
print("Is 20 adult?", Student.is_adult(20))
