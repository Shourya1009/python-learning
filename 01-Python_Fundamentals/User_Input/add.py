a = input("Enter first number : ")    # 2
b = input("Enter second number : ")   # 3

result=a+b
print(result)               # Output - 23
print(type(result))


# we want the sum of a and b so we have to convert it to integer

a=int(a)                    # 2
b=int(b)                    # 3
result=a+b
print(result)               # Output - 5
print(type(result))  


# One of the best way is to type cast it with input function
# Example :-

number_1 = int(input("Enter first number : "))    # 10
number_2 = int(input("Enter second number : "))    #20

result=number_1+number_2
print(result)               # Output - 30
print(type(result))
