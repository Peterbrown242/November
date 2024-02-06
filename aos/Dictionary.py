from math import * # sqrt pow + - * /
from datetime import datetime, date
import calendar
import pytz # python time zone 
import random

# A Dictionary is a collection which is unordered, changeable and indexed, No dulicate members.

# create Dict
person = {
    'first_name': 'John',
    'last_name': 'Mac',
    'age':       20
    
}
print(person, type(person))


# Use contructor
# person2 = dict(first_name='john', last_name='Mac')

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-554-4978'
print(person)

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# copy a dict
person2 = person.copy()
person2['state'] = 'lagos'

# Remobe an item
del(person['age'])

# pop 
person.pop('phone')

# clear
person.clear()

# Get length
print(len(person2))


# List of People
people = [
    {'name': 'Peter', 'age': 20},
    {'name': 'John', 'age': 20}
]
print(people[0]['name'])


