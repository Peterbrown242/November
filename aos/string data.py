from math import * # sqrt pow + - * /
from datetime import datetime, date
import calendar
import pytz # python time zone 
import random


# This is a comment in python. Generally for developer notes

#Date Types
#1. String Data
# name = "james"
# print(name)

# print("\n") # spacing btw 2 output
# #2. Integer Data
# my_number = 256
# print(my_number)

# print("\n")
# #3. Float Data (decimal num)
# my_float = 3.142
# print(my_float)

# print("\n")
# #4. Boolean Data (True or False)
# yes = True
# print(yes)

# print("\n")


# Strings in python are surrounded by either single or double quotes marks.. 
# Examples are Strings Formatting 
#                Strings methods 

name = "peter"
age = 37

# # concatenate
# print('Hello, my name is ' + name + ' and i am ' +   str(age) ) 

# # 
# # # Strings Formatting

# #  Arguments by position
# print('My name is {name} and i am {age}'.format(name=name, age=age))

# F-Strings (Version 3.6+)
# print(f'Hello, my name is {name} and i am {age}')



# Strings Methods

s = 'helloworld'

# Capitalize strings
print(s.capitalize())

# Make all uppercase 
print(s.upper())

# Make all lowercase 
print(s.lower())

# Swap case
print(s.swapcase())

# Get length 
print(len(s))

# Replace 
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric 
print(s.isnumeric())