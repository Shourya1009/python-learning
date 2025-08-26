"""
*args and **kwargs in Python
----------------------------

In Python, *args and **kwargs are used in function definitions 
to pass a variable number of arguments.

1. *args (Non-Keyword Arguments)
   - Allows a function to accept any number of positional arguments.
   - Inside the function, *args is treated as a tuple.

2. **kwargs (Keyword Arguments)
   - Allows a function to accept any number of keyword (named) arguments.
   - Inside the function, **kwargs is treated as a dictionary.

Use Case:
- Useful when you don’t know beforehand how many arguments will be passed.
- Increases flexibility of function definitions.
"""

# ------------------------------------------------
# Example 1: Using *args
# ------------------------------------------------
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(1, 2, 3))         
print(add_numbers(10, 20, 30, 40))  

# ------------------------------------------------
# Example 2: Using **kwargs
# ------------------------------------------------
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Shourya", age=22, city="Delhi")

# ------------------------------------------------
# Example 3: Using both *args and **kwargs
# ------------------------------------------------
def display_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

display_info(1, 2, 3, name="Shourya", course="Python")
