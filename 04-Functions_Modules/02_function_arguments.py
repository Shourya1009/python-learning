# Types of Functional Arguments :-

# 1] Positional Arguments -
# These are the most common type.
# Values are assigned to parameters based on their position in the function call.

def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("Shourya",23)



# 2]  Keyword Arguments -
# Arguments are passed using the parameter names, making the order irrelevant.
# This improves readability and avoids errors.

def keyword_argument(name, age):
    print(f"Hello {name}, you are {age} years old.")

keyword_argument(age  = 23 , name = "Shourya")



# 3] Default Arguments -
# You can assign default values to parameters in the function definition.
# If no value is provided for such arguments, the default is used.

def info(name, age=18):
    print(f"Hello {name}, you are {age} years old.")

info("Rishabh")        # Uses default age = 18
info("Shourya", 23)  # Overrides default



"""
Variable-length Arguments
These are used when you don’t know in advance how many arguments will be passed.

a] *args (Non-keyword variable-length arguments)
-> Accepts multiple positional arguments as a tuple.
"""
def sum_all(*numbers):
    print(sum(numbers))

sum_all(1, 2, 3)      # Output: 6
sum_all(5, 10, 15, 20)  # Output: 50


"""
b] **kwargs (Keyword variable-length arguments)
-> Accepts multiple keyword arguments as a dictionary.
"""
def print_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_info(name="Shourya", age=23, city="Dehradun")


