#  String Formatting :- 





# using format() method

# The format() method allows the use of simple placeholders for formatting.

# 1. Default Argument - we pass variable
name =input("Enter your name : ") 
city=input("Enter your city : ")

print("My name is {} and I live in {}.".format(name,city))


# 2. Positional Arguments - Passing the index

# Referencing variable through indexing is possible 

print("I am {0} and I am from {1}.".format(name,city))


# 3.  keyword arguments
print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346))


# 4. mixed arguments
print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346))









# Python f-string

# A Python f-string (formatted string literal) allows you to insert variables or expressions directly into a string by placing them inside curly braces {}.

# This method makes your code more readable and is often faster than other string formatting techniques.


name = "Shourya"
age = 23

# Use f-string to embed the name and age variables in a string
message=f"My name is {name} and I am {age} years old"

print(message)

# Output: My name is Shourya and I am 23 years old.



num1 = 5
num2 = 4

# Evaluate the sum of num1 and num2 inside f-string
result = f"Sum of {num1} and {num2} is {num1 + num2}."

print(result)