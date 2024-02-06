from math import * # sqrt pow + - * /
from datetime import datetime, date
import calendar
import pytz # python time zone 
import random

# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)

people = ['john', 'paul','fred','Sarah']

# simple loop

for person in people:
    print(f'current person: {person}')

# Break

for person in people:
    if person == 'fred':
       break
    print(f'current person: {person}')

# continue loop

for person in people:
    if person == 'fred':
       continue
    print(f'current person: {person}')

# range
for i in range(len(people)):
    print(people[i]) 

# custom range
for i in range(0, 11):
    print(f'numbers: {i}')
    


# while loops execute a set of statements as a condition is true.
    
count = 0
while count < 10:
    print(f'count: {count}')
    count += 1