# A function is a block of code that performs a specific task.
# The idea is to put some commonly or repeatedly done task together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.


""" 
Creating a Function in Python :- 
-> We can define a function in Python, using the def keyword. We can add any type of functionalities and properties to it as we    require.
"""


# The def keyword stands for define. It is used to create a user-defined function. It marks the beginning of a function block and allows you to group a set of statements so they can be reused when the function is called.


"""
Syntax:-

        def function_name(parameters):
        # function body
"""


"""
Explaination :-

1] def: Starts the function definition.
2] function_name: Name of the function.
3] parameters: Inputs passed to the function (inside ()), optional.
4]: -> Indicates the start of the function body.
5]Indented code: The function body that runs when called.

"""



"""
Types of Functions in Python:-

i) Built-in library function: These are Standard functions in Python that are available to use.
ii) User-defined function: We can create our own functions based on our requirements.

"""

def greet():
    print("Hello World")

# After creating a function in Python we can call it by using the name of the functions , followed by parenthesis containing arguments of that particular function. Below is the example for calling a function.

greet();



"""
 What is a Parameter in Python ?
-> A parameter is a variable used in a function definition to receive a value

What is an Argument in Python ?
-> They are the actual values passed when the function is called
"""
def greet(name):           # name is a parameter
    print("Hello",name)

greet("Shourya")           # "Shourya" is an Argument




# Function to Add Two Numbers:-

def add_numbers(num1, num2):    # ← num1 and num2 are parameters
    addition = num1+num2
    return addition

# This is Outside Function:- 
# function call 
result = add_numbers(5, 4)      # ← 5 and 4 are arguments
print(f"Sum of two numbers are {result}")



# return Statement in Python : - 
# -> In Python, we use the return statement to return a value from a function to the caller. It also ends the function’s execution immediately. 

# function definition
def find_square(num):
    result = num * num
    return result

# function call
square = find_square(3)

print(f"Square : {square}")

# Note : -  Any code after return is not executed.



"""
The pass Statement in Python :- 

The pass statement serves as a placeholder for future code, preventing errors from empty code blocks.
"""
def future_function():
    pass

# this will execute without any action or error
future_function()  
print("I am Printing after future function which does nothing")


"""
Python Library Functions :-

Python provides some built-in functions that can be directly used in our program.

Some Python library functions are:-
1] print() - prints the string inside the quotation marks
2] sqrt() - returns the square root of a number
3] pow() - returns the power of a number
4] abs() - returns the absolute value of the given number. If the number is a complex number, abs() returns its magnitude.

These library functions are defined inside the module. And to use them, we must include the module inside our program.
For example, sqrt() is defined inside the math module.
"""
import math

# sqrt computes the square root
square_root = math.sqrt(16)

print("Square Root of 16 is",square_root)

# pow() comptes the power
power = pow(4, 3)

print("4 to the power 3 is",power)


# abs() function : -

num = -17

absolute_number = abs(num)
print(absolute_number)

# Output: 17