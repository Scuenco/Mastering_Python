# Exercise: Password Checker
# At least 8 characters long
# Contains any sort letters, numbers, and the ff symbols: $%#@
# has to end with a number
import re
pattern = re.compile(r'[a-zA-Z0-9$%#@]{7,}\d$')
pwd = input('Enter your password: ')
if pattern.fullmatch(pwd):
    print("Valid password")
else:
    print("Invalid password! Must be at least 8 chars long and ends with a number.")