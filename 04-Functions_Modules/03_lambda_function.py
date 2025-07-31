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

nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4, 6]

pairs = [(1, 3), (2, 1), (4, 2)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # Output: [(2, 1), (4, 2), (1, 3)]

check_even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even_odd(7))  # Output: Odd


to_upper = lambda s: s.upper()
print(to_upper("hello"))  # Output: HELLO

