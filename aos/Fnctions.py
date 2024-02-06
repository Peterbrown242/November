from math import * # sqrt pow + - * /
from datetime import datetime, date
import calendar
import pytz # python time zone 
import random

# A Function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces.

# create a function
def sayHello(name = 'john'):
    print(f'Hello {name}')

sayHello()

# Return Value
def getans(num1, num2):
    total = num1 + num2
    return total

print(getans(3, 7)) 

# OR
num = getans(3, 7)
print(num)

# A lamda function is a small anonymous function.
# A lamda function can take any number of arguements, but can only have one expression. very similar to JS arrow functions.

getans = lambda num1, num2: num1 + num2

print(getans(10, 3))