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

# After creating a function in Python we can call it by using the name of the functions Python followed by parenthesis containing parameters of that particular function. Below is the example for calling def function Python.

greet();



"""
Python Function Arguments:-
Arguments are inputs given to the function.

"""

def greet(name):
    print("Hello", name)

# pass argument
greet("Shourya")


"""
Here, we passed 'Shourya' as an argument to the greet() function.

We can pass different arguments in each call, making the function re-usable and dynamic.
"""

greet('Rishabh')



# Function to Add Two Numbers:-

# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)

# function call 
add_numbers(5, 4)