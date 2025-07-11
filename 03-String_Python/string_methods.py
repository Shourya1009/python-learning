
# Strings are immutable in Python.
# This means once a string is created, it cannot be changed.
# If you try to modify a string (like changing a character or updating part of it), Python will instead create a new string rather than changing the original one.


name ="Harry" 
# name[0]="R"   # ❌ This will raise an error: 'str' object does not support item assignment




# In Python, len() is a built-in function that returns the number of items in an object.

# For a string, len() gives the number of characters.
# For a list, len() gives the number of elements.

name ="Shourya"
print(len(name))  # Output - 7


course="Data Science"
print(len(course))
print(course[2:-3])    # -3-1=-4 , goes from 2 to -4  
# -3+12 = 9 which is index 9
# same as [2:9]
# goes from 2 to 8 
# output will be ta Scie







# String Methods :-

# 1. upper() - Converts all lowercase characters in a string into uppercase

s="Hello WoRld"
print(len(s))
print("Upper Method")
print(s.upper())
print("Original String : ")
print(s)

# when we print the s it will remain same  that means strings are immutable in nature , and original string remain intact , it does not changed and this is immutability in action . While s.upper() return a new string 


# 2. lower() - Converts all uppercase characters in a string into lowercase

print("Lower Method")
print(s.lower(),s)


# 3. title() - Convert string to title case

print("Title Method")
print(s.title())



# 4. capitalize(): Convert the first character of a string to uppercase

print("Capitalized Method")
print(s.capitalize()) 


# 5. swapcase() - swaps the case of all characters in the string
# upper case character to lowercase and viceversa

print("Swap method")
print(s.swapcase())



# 6. strip method - Used to remove whitespaces from a string 
# i) lstrip - remove all the whitespace from the left side of the string
# ii) rstrip - remove all the whitespace from the right side of the string


print("Strip Methods : -")
text = "  hello world  "
print(text.strip()) # Output: "hello world"
print(text.lstrip()) # Output: "hello world  "
print(text.rstrip()) # Output: "  hello world"



#7. Find and Replace :-

# find(word or string to be find)  - return index of the first character of the word or string
# replace("original word" , "new word") - return string with the replaced word

print("Find and Replace Method :")
txt="Python is fun"
print(txt.find("fun"))
print("Original string : ",txt)
print("Replaced String : ",txt.replace("fun","awesome"))






# 8. Split and Join : 

# The split() method breaks down a string into a "list of substrings" using a chosen separator , default is whitespace

text = 'Python is fun'

# It will seperate the string into a list of substring from the whitespace as no seperator is specified 

# split the text from space
print(text.split())

# Output: ['Python', 'is', 'fun']





# split() Syntax :-
# str.split(separator, maxsplit)





# split() Parameters :-

# The split() method takes a maximum of 2 parameters:

# separator (optional) - Specifies the delimiter( A delimiter is a character or symbol used to separate distinct pieces of data in a string or text) used to split the string. If not provided, whitespace is used as the default delimiter.

# maxsplit (optional) - Determines the maximum number of splits. If not provided, the default value is -1, which means there is no limit on the number of splits.





# split() Return Value:-
# The split() method returns a " list " of strings.


text1 = 'Split this string'

# splits using space
print(text1.split())

grocery = 'Milk, Chicken, Bread'

# splits using ,
print(grocery.split(', '))

# splits using :
# doesn't split as grocery doesn't have :
print(grocery.split(':'))


# text.split() - splits the string into a list of substrings at each space character.
# grocery.split(', ') - splits the string into a list of substrings at each comma and space character.
# grocery.split(':') - since there are no colons in the string, split() does not split the string.






# We can use the maxsplit parameter to limit the number of splits that can be performed on a string.

grocery = 'Milk#Chicken#Bread#Butter'

# maxsplit: 1
print(grocery.split('#', 1))

# maxsplit: 2
print(grocery.split('#', 2))

# maxsplit: 5
print(grocery.split('#', 5))

# maxsplit: 0
print(grocery.split('#', 0))






# Join in python :-

# The string join() method returns a string by joining all the elements of an iterable (list, string, tuple), separated by the given separator.

text = ['Python', 'is', 'a', 'fun', 'programming', 'language']
print(type(text))

# join elements of text with space
print(' '.join(text))

# Output: Python is a fun programming language


# join elements of text with special symbol(@)
print(' @ '.join(text))



# The syntax of the join() method is:-
# string.join(iterable)



# The join() method takes an iterable (objects capable of returning its members one at a time) as its parameter.
# Some of the example of iterables are:
# Native data types - List, Tuple, String, Dictionary and Set.






# Return Value from join() :-

# The join() method returns a string created by joining the elements of an iterable by the given string separator.
# If the iterable contains any non-string values, it raises the TypeError exception.













# isaplha() :-

# The isalpha() returns:
# True if all characters in the string are alphabets (can be both lowercase and uppercase).
# False if at least one character is not alphabet.

name = "Monica"
print(name.isalpha())

# contains whitespace
name = "Monica Geller"
print(name.isalpha())

# contains number
name = "Mo3nicaGell22er"
print(name.isalpha())



name = "MonicaGeller"

if name.isalpha() == True:
   print("All characters are alphabets")
else:
    print("All characters are not alphabets.")




# isdigit() :-

# The isdigit() returns:
# True if all characters in the string are digits.
# False if at least one character is not a digit.


s = "28212"
print(s.isdigit())

# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.isdigit())






# isalnum() :-
# Return true if string is alpha numeric and false if not aplha numeric

sol ="Python123"
print(sol.isalnum())




# isspace() :-

# Return true if string is a whitespace string , false otherwise 

print(sol.isspace())