"""
Decorators in Python
--------------------

A decorator in Python is a function that modifies the behavior of another function
or method without permanently changing it.

Key Points:
- Functions in Python are first-class objects (they can be passed as arguments, returned from functions, and assigned to variables).
- Decorators allow adding extra functionality (logging, authentication, timing, etc.) to existing functions in a clean and reusable way.
- Defined using the `@decorator_name` syntax above a function.

-------------------------------------------------
Basic Decorator Example
-------------------------------------------------
"""

# A simple decorator
def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, World!")

say_hello()

"""
Output:
Before the function is called.
Hello, World!
After the function is called.
"""

# ------------------------------------------------
# Decorator with Arguments
# ------------------------------------------------

def greet_decorator(func):
    def wrapper(name):
        print("Preparing to greet...")
        func(name)
        print("Greeting finished.")
    return wrapper

@greet_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

"""
Output:
Preparing to greet...
Hello, Alice!
Greeting finished.
"""

# ------------------------------------------------
# Real-world Example: Timing a Function
# ------------------------------------------------
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.5f} seconds")
        return result
    return wrapper

@timer
def calculate_square(numbers):
    return [n*n for n in numbers]

print("\nTiming Example:")
print(calculate_square(range(1, 10000)))
