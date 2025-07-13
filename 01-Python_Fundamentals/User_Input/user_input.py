# To take user input we use built in function which is input() function which take input as a string 
# Syntax - input(prompt) - prompt is just a string enclosed within quotes

 
a=input("Enter a Number : ")  # input always taken as string 
print(a)
print(type(a))

num = int(input("Enter a number : "))
print(f"The number you have entered is {num}")
print(type(num))

name = input("Enter your name : ")
age = int(input("Enter your age : "))
print("Your name is {} and you age is {}".format(name,age))
print(f"Your age is {age} and your name is {name}")