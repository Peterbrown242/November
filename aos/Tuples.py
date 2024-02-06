from math import * # sqrt pow + - * /
from datetime import datetime, date
import calendar
import pytz # python time zone 
import random

 # Tuple Creation: Tuples in Python are immutable, meaning you cannot modify their elements after creation.
 # Tuple is a colection which is ordered and unchangeable. Allows duplicate members.


 # Use a tuple when you have a fixed collection of elements that should not be modified.
 # If immutability is desired, or if the collection represents a fixed set of values, 
# then a tuple may be more appropriate.



fruits = ('Apple', 'Banana', 'Mango', 'Orange', 'Grapes') # 
# fruits2 = ('Apple', 'Banana', 'Mango', 'Orange', 'Grapes') 

# Single value needs traling comma
fruits2 = ('Apple',)

print(fruits2, type(fruits2))

# Get value
print(fruits[1])

# Can't change value
# fruits[0] = 'pears'

# Delete tuple
del fruits2


# Get length 
print(len(fruits))


# Reassignment/ Add to Tuples
fruits = fruits + ('pears',)
print(fruits)

# A set is a collection which is unordered and unindexed. No duplicate members.

# create a set
fruits_set = {'Apple', 'Banana', 'Mango', 'Orange', 'Grapes'}

# Check if in set
print('Apple' in fruits_set)

# Add to set
fruits_set.add('lemon')
print(fruits_set)

# Add duplicates to set
fruits_set.add('apple')

# Remove from set
fruits_set.remove('Apple')
print(fruits_set)

# clear set
fruits_set.clear()
print(fruits_set)

# delete set
# del fruits_set
# print(fruits_set)


