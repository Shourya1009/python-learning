# Variable - > is a named reference to a value stored in memory , allowing data to be accessed and modified during program execution.

# Variable are named containers to hold data values.

# Python does not store values directly in variables like in some other languages; instead, it stores references (or pointers) to objects.

# In Python a variable is created when we assign a value to it .

age = 23 #integer
name = "Shourya" #String
cgpa = 8.9 #float


# Data types in Python 

# Integer(int) - Whole numbers (eg - 10,-5)
# Float(float) - Decimal Number ( eg -  3.14,2.5,-0.0032 )
# String(str) - text data enclosed in quotes ( eg - "Hello" , 'Python')
# Boolean(bool) - Represent true or false
# Complex(complex) -> Represent complex number in form of (a+bj) where a is real number and b is imagin


age=3
print(age)
print(type(age))  #int

cgpa=9.2
print(cgpa)
print(type(cgpa))  #float

name="Aman"
print(name)
print(type(name))  #str


is_completed=True
print(is_completed)
print(type(is_completed))   #bool


work_done=False
print(work_done)
print(type(work_done))

complex_datatype = 6+7j
print("Data type : ",type(complex_datatype))
