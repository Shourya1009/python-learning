
# Type Casting is the method to convert the Python variable datatype into a certain data type in order to perform the required operation by users.

# There can be two types of Type Casting in Python:

# 1] Python Implicit Type Conversion
# 2] Python Explicit Type Conversion

# 1] Implicit Type Conversion in Python
# -> In this, method, Python converts the datatype into another datatype automatically. Users don't have to involve in this process. 

# 2] Explicit Type Conversion in Python
# -> In this method, Python needs user involvement to convert the variable data type into the required data type. 


# Mainly type casting can be done with these data type functions:-
# Int(): Python Int() function take float or string as an argument and returns int type object.
# float(): Python float() function take int or string as an argument and return float type object.
# str(): Python str() function takes float or int as an argument and returns string type object.


a=34 
print(a)
print(type(a))

b="34"
print(b)
print(type(b))


# convert b to an integer
c=int(b)
print(type(c))

d=223
print(d)
print(type(d))

e=str(d)
print(e)
print(type(e))



#convert string to integer

num_str="10"
num_int=int(num_str)
print(num_int)              # Output - 10
print(type(num_int)) 


# convert int to string

num=25
num_str=str(num)
print(num_str)              # Output - 25
print(type(num_str))


# convert float to integer

pi=3.14
pi_int=int(pi)
print(pi_int)               # Output- 3
print(type(pi_int))

