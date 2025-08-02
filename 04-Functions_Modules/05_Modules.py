# Module is a file that contains code to perform a specific task. A module may contain variables, functions, classes etc.



# Let us create a module. Type the following and save it as example.py.
# Python Module addition
def add(a, b):

   result = a + b
   return result

# Here, we have defined a function add() inside a module named example. The function takes in two numbers and returns their sum.


# Import Python Standard Library Modules :-

"""
The Python standard library contains well over 200 modules. We can import a module according to our needs.

Suppose we want to get the value of pi, first we import the math module and use math.pi. For example,
"""

# import standard math module 
import math

# use math.pi to get value of pi
print("The value of pi is", math.pi)



# Python import with Renaming
# In Python, we can also import a module by renaming it. For example,

# import module by renaming it
import math as m

print(m.pi)

# Output: 3.141592653589793