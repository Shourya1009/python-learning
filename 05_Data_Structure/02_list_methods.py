"""

A list method in Python is a built-in function that belongs to the list data type and is used to perform operations on list objects.

Think of it like this:

1] A list is a container for storing multiple items.

2] List methods are special tools you can use to add, remove,       search, sort, or manipulate those items.

"""


# 1. append() - Add element at the end
fruits = ["apple", "banana"]
fruits.append("cherry")
print("append():", fruits)

# 2. insert() - Insert element at specific position
fruits.insert(1, "orange")
print("insert():", fruits)

# 3. extend() - Add elements from another iterable
fruits.extend(["mango", "grape"])
print("extend():", fruits)

# 4. remove() - Remove first occurrence of a value
fruits.remove("banana")
print("remove():", fruits)

# 5. pop() - Remove and return element at given index (default last)
popped_item = fruits.pop()
print("pop():", fruits, "| Popped:", popped_item)

# 6. clear() - Remove all elements
temp_list = [1, 2, 3]
temp_list.clear()
print("clear():", temp_list)

# 7. index() - Get index of first occurrence
numbers = [10, 20, 30, 20]
print("index():", numbers.index(20))

# 8. count() - Count occurrences of a value
print("count():", numbers.count(20))

# 9. sort() - Sort list in ascending order
numbers.sort()
print("sort():", numbers)

# 10. reverse() - Reverse the list
numbers.reverse()
print("reverse():", numbers)

# 11. copy() - Shallow copy of a list
numbers_copy = numbers.copy()
print("copy():", numbers_copy)