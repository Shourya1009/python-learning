"""
Static Methods and Class Methods in Python
------------------------------------------

In Python, apart from instance methods, we can also define methods that
belong to the class itself rather than to individual objects.

1. Instance Method (default):
   - The most common type of method.
   - Takes `self` as the first argument.
   - Can access and modify instance attributes.
   - Can also access class attributes.

2. Class Method:
   - Defined using the `@classmethod` decorator.
   - Takes `cls` (class) as the first argument.
   - Can access and modify class attributes.
   - Cannot directly access instance attributes.
   - Often used as factory methods (alternative constructors).

3. Static Method:
   - Defined using the `@staticmethod` decorator.
   - Does not take `self` or `cls`.
   - Works like a normal function but belongs to the class.
   - Cannot modify class or instance attributes directly.
   - Used for utility/helper functions.

-------------------------------------------------
Example Code
-------------------------------------------------
"""

class Student:
    school_name = "ABC School"  # Class Attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance Method
    def display(self):
        print(f"Name: {self.name} | Age: {self.age} | School: {Student.school_name}")

    # Class Method (modify class attribute)
    @classmethod
    def change_school(cls, new_name):
        print(f"\n[INFO] Changing school to: {new_name}")
        cls.school_name = new_name

    # Class Method (Factory Method)
    @classmethod
    def from_string(cls, student_str):
        name, age = student_str.split("-")
        return cls(name.strip(), int(age))

    # Static Method (utility function)
    @staticmethod
    def is_adult(age):
        return age >= 18

    # Another Static Method
    @staticmethod
    def is_valid_age(age):
        return 0 < age < 100


# Demonstration
s1 = Student("Shourya", 17)
s2 = Student("Anuj", 20)

# Using factory method
s3 = Student.from_string("Riya-22")

print("\n--- Initial Data ---")
for student in (s1, s2, s3):
    student.display()

# Class Method usage
Student.change_school("XYZ School")

print("\n--- After Changing School ---")
for student in (s1, s2, s3):
    student.display()

# Static Methods
print("\n--- Static Method Outputs ---")
for age in (17, 20, 150):
    print(f"Age {age} -> Adult: {Student.is_adult(age)}, Valid: {Student.is_valid_age(age)}")