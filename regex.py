"""
import re
str = 'search this inside of this text please! Sherry'
a = re.search('this', str)
print(a.span()) #(17, 21); #specifies where the string occurs as a tuple
print(a.start()) #17
print(a.end()) #21

pattern = re.compile('this')
a = pattern.search(str)
b = pattern.findall(str)
c = pattern.fullmatch(str)
d = pattern.match(str)
print(a.group()) #this
print(b) #['this', 'this']
print(c) #None
print(d) #None """

""" pattern = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
str = 'Sherry@test.com'
a = pattern.search(str)
print(a) """

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