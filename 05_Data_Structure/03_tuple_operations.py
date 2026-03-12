# 📌 Tuples and Operations in Python

# A tuple is an ordered and immutable collection of elements.
# It can store different data types and allows duplicate values.

# -------------------------------------------------
# Creating Tuples
# -------------------------------------------------
empty_tuple = ()
numbers_tuple = (1, 2, 3)
tuple_without_parentheses = 4, 5, 6
mixed_tuple = (1, "Hello", 3.5)
nested_tuple = (1, (2, 3), (4, 5))

print("Numbers tuple:", numbers_tuple)
print("Mixed tuple:", mixed_tuple)
print("Nested tuple:", nested_tuple)

# -------------------------------------------------
# Accessing Elements
# -------------------------------------------------
t = (10, 20, 30, 40)

print("\nFirst element:", t[0])
print("Last element:", t[-1])
print("Slice from index 1 to 2:", t[1:3])

# -------------------------------------------------
# Concatenation and Repetition
# -------------------------------------------------
a = (1, 2)
b = (3, 4)

print("\nConcatenation:", a + b)
print("Repetition:", a * 3)

# -------------------------------------------------
# Membership Test
# -------------------------------------------------
print("\nIs 20 present in tuple?", 20 in t)
print("Is 50 not present in tuple?", 50 not in t)

# -------------------------------------------------
# Iterating Through a Tuple
# -------------------------------------------------
print("\nIterating through tuple:")
for value in (1, 2, 3):
    print(value)

# -------------------------------------------------
# Built-in Tuple Functions
# -------------------------------------------------
t2 = (5, 1, 5, 3)

print("\nLength of tuple:", len(t2))
print("Maximum value:", max(t2))
print("Minimum value:", min(t2))
print("Count of 5:", t2.count(5))
print("Index of 3:", t2.index(3))

# -------------------------------------------------
# Practical Example
# -------------------------------------------------
coordinates = (4, 5)
print(f"\nCoordinates -> X: {coordinates[0]}, Y: {coordinates[1]}")

# -------------------------------------------------
# Why Use Tuples?
# -------------------------------------------------
# 1. Tuples are faster than lists because they are immutable.
# 2. They can be used as keys in dictionaries.
# 3. Suitable for storing fixed data that should not change.