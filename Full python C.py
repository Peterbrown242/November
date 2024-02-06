from math import * # sqrt pow + - * /
from datetime import datetime, date
import calendar
import pytz # python time zone 
import random






# A varaible is a container for a value, which can be of various types

# Variable Rules 
# - Variable names are case sentitive (name and NAME are different variables)
# - Must start with a letter or an underscore
# - Can have numbers but not start with one 


# x = 1                    # integer
# y = 2.5                   #float 
# name = 'peter'            # string
# is_cool = True               # boolean

# multiple assisgnmet 
x, y, name, is_cool = (1, 2.5 , 'peter', True)

print(x, y, name, is_cool)

# basic math 
a = x + y 
print(a)

# Casting
x =  str(x)
y = int(y)
z = float(y)

print(type(z), z)
