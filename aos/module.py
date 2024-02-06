from math import * # sqrt pow + - * /
from datetime import datetime, date
import calendar
import pytz # python time zone 
import random

# A module is basically a file containig a set of functions to include in your application. 
# there are core python modules. modules you can install using pip package manager 
# (including Django) as well as custom modules

# Core modules available by python
import datetime
# or
from datetime import date
import time
# or
from time import time

# pip module
from camelcase import CamelCase




# Import custom module
import validator
from validator import validate_email

# today = datetime.date.today()
# or

today = date.today()
# or
timestamp = time()


c = CamelCase()
# print(c.hump('hello there world'))

# email = 'test@test.com'
# if validate_email(email):
#     print('Email is valid')
# else:
#     print('Email is invalid')




# print(timestamp)


# from validator import validate_num
# define number in list 
valid_numbers = [1, 2, 3, 4, 5, 6, 7]

# number to validate
numbers_to_validate = [2, 3, 5, 6]
if all(number in valid_numbers for number in numbers_to_validate):
    print(f'All number {numbers_to_validate} is valid')
else:
    print(f'some or all number {numbers_to_validate} is invalid')







# valid_number = [1, 2, 3, 4, 5, 6, 7]  # Replace 5 with the number you want to validate

# number_to_validate = 6

# if number_to_validate in valid_number:
#     print(f'{number_to_validate} is valid')
# else:
#     print(f'{number_to_validate} is invalid') 


