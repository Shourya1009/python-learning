# Ord function

# The ord() function returns an integer representing the Unicode character.

character = 'P'

# find unicode of P
unicode_char = ord(character)
print(unicode_char)

# Output: 80



# Ord() Syntax

# The syntax of ord() is:
# ord(ch)


print(ord('5'))    # 53
print(ord('A'))    # 65
print(ord('$'))    # 36
print(ord('S'))
print(ord('K'))
print(ord('@'))
print(ord('*'))





# chr() function 

# The chr() method converts an integer to its unicode character and returns it.



# chr() Parameter
# The chr() method takes in a single parameter:
# number - an integer number in the range 0 to 1,114,111

print(chr(97))
# Output: a

print(chr(98))
#  Output: b

print(chr(65))
# Output : A

print(chr(89))
# Ouput - 89

print(chr(58))
# Output - :

print(chr(165))
# Output - ¥

print(chr(198))
# Output - Æ