# Conditional Statement - used to execute a certain block of code based on specific condition.

'''
1] If conditional statement :- execute a block of code if condition given is true.
'''
age =20
if age>=18:
    print("Elgible to Vote")  


'''
2] Else conditional statement :- execute a block of code if condition associated with if and wlig block evaluated to False.
'''
age_1=15
if age_1<=12:
    print("Travel for free")
else:
    print("Pay for Ticket")


'''
3] elif conditional statement :-

i) In Python elif stands for "else if"

ii) It allows us to check for multiple conditions ,providing a way to execute different block of code based on which condition is true

iii) It makes our code more readable and efficient by eliminating the use of multiple nested if statement.

'''
age_2=25
if age_2<=12:
    print("Chld")
elif age_2<=19:
    print("Teenager")
elif age_2<=35:
    print("Adult")
else:
    print("Senior Citizen ")