"""
Python Dictionary & Its Methods
"""

# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print("Original Dictionary:", my_dict)

# Accessing values
print("Name:", my_dict["name"])
print("City:", my_dict.get("city"))

# Adding or updating a key-value pair
my_dict["email"] = "alice@example.com"
my_dict["age"] = 26
print("After adding/updating:", my_dict)

# Removing items
my_dict.pop("city")         # Removes key and returns value
print("After pop:", my_dict)

del my_dict["email"]        # Deletes key
print("After del:", my_dict)

removed_item = my_dict.popitem()  # Removes last inserted key-value pair
print("After popitem:", my_dict)
print("Removed item:", removed_item)

# Dictionary methods
sample_dict = {"a": 1, "b": 2, "c": 3}

print("Keys:", sample_dict.keys())          # Returns all keys
print("Values:", sample_dict.values())      # Returns all values
print("Items:", sample_dict.items())        # Returns key-value pairs

# Copying a dictionary
dict_copy = sample_dict.copy()
print("Copied dict:", dict_copy)

# Updating a dictionary
sample_dict.update({"d": 4, "a": 10})
print("After update:", sample_dict)

# Clearing a dictionary
sample_dict.clear()
print("After clear:", sample_dict)

"""
Common Dictionary Methods:
- dict.get(key, default) → Returns value if key exists, else default
- dict.keys() → Returns all keys
- dict.values() → Returns all values
- dict.items() → Returns (key, value) pairs
- dict.update(other_dict) → Merges another dictionary
- dict.pop(key, default) → Removes key and returns value
- dict.popitem() → Removes last inserted pair
- dict.copy() → Returns a shallow copy
- dict.clear() → Removes all items
"""
