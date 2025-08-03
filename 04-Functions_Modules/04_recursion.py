# In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.

# The following image shows the working of a recursive function called recurse.

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 3
print("The factorial of", num, "is", factorial(num))



# Factorial of a number :-
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)



# Fibonacci Series
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)



# Sum of Digits
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)



# Reverse a String
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]


# Palindrome
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
