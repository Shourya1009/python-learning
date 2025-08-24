"""
Map, Filter, and Reduce in Python
---------------------------------

These are functional programming tools in Python that allow us 
to apply functions to iterables like lists and tuples.

1. map(function, iterable)
   - Applies a function to each item in the iterable
   - Returns a map object (convertible to list, tuple, etc.)

2. filter(function, iterable)
   - Filters elements of an iterable based on a condition
   - Returns a filter object with only items where the function returns True

3. reduce(function, iterable)
   - Repeatedly applies a function to the items of the iterable
   - Returns a single cumulative value
   - Must be imported from functools
"""

from functools import reduce

# ------------------------------------------------
# Example: map()
# ------------------------------------------------
numbers = [1, 2, 3, 4, 5]

# Square each number using map
squared = list(map(lambda x: x**2, numbers))
print("Original numbers:", numbers)
print("Squared numbers (map):", squared)

# ------------------------------------------------
# Example: filter()
# ------------------------------------------------
# Get only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers (filter):", evens)

# ------------------------------------------------
# Example: reduce()
# ------------------------------------------------
# Find product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print("Product of numbers (reduce):", product)
