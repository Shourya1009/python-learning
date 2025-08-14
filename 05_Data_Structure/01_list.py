'''
A list in Python is a built-in data structure that allows you to store multiple values in a single variable. It is:

i] Ordered: Elements have a defined order.

ii] Mutable: You can change, add, or remove items.

iii] Allows duplicates: You can store the same value more than once.

iv] Can store different data types: Including numbers, strings, booleans, or even other lists.

'''

# A list of numbers
numbers = [10, 20, 30]

# A list of strings
fruits = ["apple", "banana", "cherry"]

# A mixed data type list
mixed = [1, "hello", 3.14, True]

# A list inside another list (nested)
nested = [1, [2, 3], 4]




my_list = [1, 2, 3]

print(my_list[0])    # Access first element → 1
my_list.append(4)    # Add 4 → [1, 2, 3, 4]
my_list.remove(2)    # Remove 2 → [1, 3, 4]
my_list[1] = 10      # Change second element → [1, 10, 4]
print(len(my_list))  # Length → 3




shopping_list = ["milk", "bread", "eggs"]

for item in shopping_list:
    print(f"I need to buy {item}")
