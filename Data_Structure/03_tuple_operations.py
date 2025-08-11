# 📌 Tuple and Its Operations in Python

# A tuple is an ordered, immutable collection of elements.
# It can store mixed data types and allows duplicates.

# Creating Tuples
empty_tuple = ()
tuple_with_values = (1, 2, 3)
tuple_without_parentheses = 4, 5, 6
mixed_tuple = (1, "Hello", 3.5)
nested_tuple = (1, (2, 3), (4, 5))

# Accessing Elements
t = (10, 20, 30, 40)
print("First element:", t[0])
print("Last element:", t[-1])
print("Slicing (1:3):", t[1:3])

# Concatenation & Repetition
a = (1, 2)
b = (3, 4)
print("Concatenation:", a + b)
print("Repetition:", a * 3)

# Membership Test
print("20 in t:", 20 in t)
print("50 not in t:", 50 not in t)

# Iteration
print("Iterating through tuple:")
for item in (1, 2, 3):
    print(item)

# Tuple Functions
t2 = (5, 1, 5, 3)
print("Length:", len(t2))
print("Max:", max(t2))
print("Min:", min(t2))
print("Count of 5:", t2.count(5))
print("Index of 3:", t2.index(3))

# Example Use Case
coordinates = (4, 5)
print(f"Coordinates -> X: {coordinates[0]}, Y: {coordinates[1]}")

# 📍 Why Tuples?
# - Faster than lists (due to immutability)
# - Can be used as dictionary keys
# - Ideal for fixed data that should not change
