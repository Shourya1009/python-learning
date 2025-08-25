"""
Walrus Operator (:=) in Python
------------------------------

Introduced in Python 3.8, the Walrus Operator allows assignment 
and evaluation in a single expression. It is also called the 
"assignment expression".

Key points:
1. Assigns a value to a variable as part of an expression.
2. Reduces redundancy by avoiding repeating the same expression.
3. Often used in loops, conditions, and comprehensions.

Syntax:
    variable := expression
"""

# ------------------------------------------------
# Example 1: Using without Walrus
# ------------------------------------------------
text = input("Enter text: ")
while text != "quit":
    print("You entered:", text)
    text = input("Enter text: ")

# ------------------------------------------------
# Example 2: Using Walrus Operator
# ------------------------------------------------
while (text := input("Enter text: ")) != "quit":
    print("You entered:", text)

# ------------------------------------------------
# Example 3: In a List Comprehension
# ------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6]

# Without Walrus
squares = [n**2 for n in numbers if n**2 > 10]

# With Walrus
squares_walrus = [sq for n in numbers if (sq := n**2) > 10]

print("Squares without walrus:", squares)
print("Squares with walrus:", squares_walrus)
