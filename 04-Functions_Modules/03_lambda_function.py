# A lambda function in Python is a small, anonymous function defined using the lambda keyword. It is typically used when you need a simple function for a short period and don’t want to formally define it using def.



# Syntax:- lambda arguments: expression
# -> It can have any number of arguments but only one expression.
# -> The result of the expression is automatically returned.


add = lambda x, y: x + y
print(add(3, 5))  
# Output: 8

square = lambda x: x*x
print(square(3))
# Output: 9