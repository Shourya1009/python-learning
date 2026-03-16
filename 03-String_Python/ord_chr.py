# ------------------------------------
# ord() Function in Python
# ------------------------------------
# The ord() function returns the Unicode value (integer)
# of a given character.

character = 'P'

# Find Unicode value of 'P'
unicode_char = ord(character)
print("Unicode of P:", unicode_char)   # Output: 80


# Examples of ord()
print("Unicode of '5':", ord('5'))   # 53
print("Unicode of 'A':", ord('A'))   # 65
print("Unicode of '$':", ord('$'))   # 36
print("Unicode of 'S':", ord('S'))   # 83
print("Unicode of 'K':", ord('K'))   # 75
print("Unicode of '@':", ord('@'))   # 64
print("Unicode of '*':", ord('*'))   # 42


# ------------------------------------
# chr() Function in Python
# ------------------------------------
# The chr() function converts a Unicode integer
# into its corresponding character.

print("chr(97):", chr(97))    # a
print("chr(98):", chr(98))    # b
print("chr(65):", chr(65))    # A
print("chr(89):", chr(89))    # Y
print("chr(58):", chr(58))    # :
print("chr(165):", chr(165))  # ¥
print("chr(198):", chr(198))  # Æ