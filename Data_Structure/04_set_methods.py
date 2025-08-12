"""
Python Set and Its Methods
--------------------------
A set is an unordered collection of unique elements in Python.

Properties:
- Unordered: No guaranteed order of elements.
- Unique: Duplicate values are automatically removed.
- Mutable: You can add or remove elements after creation.
"""

# Creating Sets
set1 = {1, 2, 3}
set2 = set([1, 2, 2, 3])  # Duplicates removed -> {1, 2, 3}

print("Initial Sets:")
print("set1:", set1)
print("set2:", set2)

# -----------------------
# Common Set Methods
# -----------------------

# add()
set1.add(4)
print("\nAfter add(4):", set1)

# remove()
set1.remove(2)  # Raises KeyError if element not found
print("After remove(2):", set1)

# discard()
set1.discard(10)  # No error if element is missing
print("After discard(10):", set1)

# pop()
popped_item = set1.pop()
print(f"Popped item: {popped_item}")
print("After pop():", set1)

# copy()
set_copy = set1.copy()
print("Copy of set1:", set_copy)

# update()
set1.update([5, 6])
print("After update([5, 6]):", set1)

# union()
A = {1, 2, 3}
B = {3, 4, 5}
print("\nUnion A | B:", A.union(B))

# intersection()
print("Intersection A & B:", A.intersection(B))

# difference()
print("Difference A - B:", A.difference(B))

# symmetric_difference()
print("Symmetric Difference A ^ B:", A.symmetric_difference(B))

# issubset()
print("A is subset of B?", A.issubset(B))

# issuperset()
print("A is superset of B?", A.issuperset(B))

# isdisjoint()
print("A and B are disjoint?", A.isdisjoint(B))

# clear()
set1.clear()
print("\nAfter clear():", set1)
