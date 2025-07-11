# it is similar to switch case statement

# Default Value
# Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:

day=int(input("Enter a day number : "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:                                                     # this is a default case - works only when , no other cases work 
        print("Looking forward to the Weekend")
    

# The value _ will always match, so it is important to place it as the last case to make it beahave as a default case.



# Combine Values
# Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:


day = int(input("Enter a day : "))
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")





# If Statements as Guards
# You can add if statements in the case evaluation as an extra condition-check:


month = int(input("Enter a month : "))
day = int(input("Enter a DAY : "))
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")