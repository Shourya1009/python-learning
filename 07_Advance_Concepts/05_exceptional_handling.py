"""
Exception Handling and Custom Errors in Python
----------------------------------------------

Exceptions are runtime errors that occur during program execution.
Python provides a way to handle these errors gracefully using
`try`, `except`, `else`, and `finally` blocks.

Basic keywords:
- try: Code that might raise an error
- except: Code to handle the error
- else: Code that runs if no error occurs
- finally: Code that always runs (cleanup tasks)

-------------------------------------------------
Example: Built-in Exception Handling
-------------------------------------------------
"""

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        result = None
    except TypeError:
        print("Error: Invalid input type.")
        result = None
    else:
        print("Division successful!")
    finally:
        print("Execution completed.")
    return result

print("Result:", divide(10, 2))
print("Result:", divide(10, 0))
print("Result:", divide(10, "five"))

"""
-------------------------------------------------
Custom Exceptions
-------------------------------------------------
We can also define our own exceptions by creating a class
that inherits from the built-in `Exception` class.
"""

class NegativeNumberError(Exception):
    """Custom exception for handling negative numbers."""
    pass

def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    return number

try:
    print(check_positive(10))
    print(check_positive(-5))
except NegativeNumberError as e:
    print("Custom Error Caught:", e)