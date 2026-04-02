"""
List Methods in Python
----------------------

A list method is a built-in function associated with Python lists.
These methods help you manipulate list data easily.

Think of it like:
1. A list = a container of items
2. Methods = tools to operate on those items
"""

# Initial list
fruits = ["apple", "banana"]
print("Original list:", fruits)


# 1. append() → Adds element at the end
fruits.append("cherry")
print("\nappend():", fruits)


# 2. insert() → Adds element at a specific index
fruits.insert(1, "orange")
print("insert():", fruits)


# 3. extend() → Adds multiple elements
fruits.extend(["mango", "grape"])
print("extend():", fruits)


# 4. remove() → Removes first matching value
fruits.remove("banana")
print("remove():", fruits)


# 5. pop() → Removes & returns element (default: last)
popped_item = fruits.pop()
print("pop():", fruits, "| Popped item:", popped_item)


# 6. clear() → Removes all elements
temp_list = [1, 2, 3]
temp_list.clear()
print("\nclear():", temp_list)


# New list for numeric operations
numbers = [10, 20, 30, 20]
print("\nNumbers list:", numbers)


# 7. index() → Returns index of first occurrence
print("index():", numbers.index(20))


# 8. count() → Counts occurrences
print("count():", numbers.count(20))


# 9. sort() → Sorts list (ascending by default)
numbers.sort()
print("sort():", numbers)


# 10. reverse() → Reverses the list
numbers.reverse()
print("reverse():", numbers)


# 11. copy() → Creates a shallow copy
numbers_copy = numbers.copy()
print("copy():", numbers_copy)