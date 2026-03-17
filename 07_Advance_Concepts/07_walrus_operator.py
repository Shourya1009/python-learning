"""
Walrus Operator (:=) in Python
------------------------------

Introduced in Python 3.8, the Walrus Operator allows assignment 
and evaluation in a single expression. It is also called the 
"assignment expression".

Key Points:
1. Assigns a value to a variable inside an expression.
2. Helps reduce repetition of the same computation.
3. Commonly used in loops, conditions, and comprehensions.

Syntax:
    variable := expression
"""

# ------------------------------------------------
# Example 1: Without Walrus Operator
# ------------------------------------------------
text = input("Enter text (type 'quit' to stop): ")

while text != "quit":
    print("You entered:", text)
    text = input("Enter text (type 'quit' to stop): ")

# ------------------------------------------------
# Example 2: Using Walrus Operator
# ------------------------------------------------
while (text := input("Enter text (type 'quit' to stop): ")) != "quit":
    print("You entered:", text)

# ------------------------------------------------
# Example 3: List Comprehension
# ------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6]

# Without Walrus
squares = [n**2 for n in numbers if n**2 > 10]

# With Walrus (avoids recalculating n**2)
squares_walrus = [sq for n in numbers if (sq := n**2) > 10]

print("Squares without walrus:", squares)
print("Squares with walrus:", squares_walrus)

# ------------------------------------------------
# Example 4: Using Walrus in Condition
# ------------------------------------------------
# Find length of input and check in one line
if (length := len(text)) > 5:
    print(f"Last input had {length} characters (more than 5)")
else:
    print(f"Last input had {length} characters (5 or less)")