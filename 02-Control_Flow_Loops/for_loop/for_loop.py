# A for loop is used for iterating over a sequence 
# (such as a list, tuple, dictionary, set, or string).

# It is a bit different from other programming languages,
# and works more like an iterator method in object-oriented languages.

# With a for loop, we can execute a block of statements
# once for each item in a sequence.


# Syntax of for loop in Python :-

# for variable_name in range(start, end):
#     statements


# Print numbers from 1 to 10 using for loop

for i in range(1, 11):
    print(i)


# Print table of 5 using for loop 

for x in range(1, 11):
    result = 5 * x
    print("5 *", x, "=", result)