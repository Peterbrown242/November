from math import * # sqrt pow + - * /
from datetime import datetime, date
import calendar
import pytz # python time zone 
import random

# A List is a collection which is ordered and changeable. Allows duplicate members
# # Lists in Python are mutable, meaning you can modify their elements after creation. 



#  list Creation 
numbers = [ 1, 2, 3, 4, 5 ]
fruits = ['Apple', 'Banana', 'Mango', 'Orange', 'Grapes']


# Choosing Between Lists and Tuples:

# Use a list when you need a mutable sequence of elements.

# In general, if you need to modify the collection frequently, a list is a better choice. 



 # Tuple Creation: Tuples in Python are immutable, meaning you cannot modify their elements after creation.
# fruits = ('Apple', 'Banana', 'Mango', 'Orange', 'Grapes') # 

# # use a constructor
# numbers2 = list((1, 2, 3, 4, 5))

# print(numbers, numbers2)

# Get a Value
print(fruits[2])

# Get length 
print(len(fruits))

# Append to list
fruits.append('Pears')
print(fruits)



 # Remove from list
fruits.remove('Orange')
print(fruits)

#Insert into position
fruits.insert(2, 'Strawberries')
print(fruits)

# Remove with pop
fruits.pop(2)
print(fruits)

# Reverse list
fruits.reverse()
print(fruits)

# Sort list
fruits.sort()
print(fruits)

# Change Value
fruits[0] = 'Blueberries'
print(fruits)