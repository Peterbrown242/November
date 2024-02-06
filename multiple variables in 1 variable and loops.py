from math import * # sqrt pow + - * /
from datetime import datetime, date
import calendar
import pytz # python time zone 
import random







#------Python List -------(Sorage of multiples values in a single variable)
#           -5       -4       -3        -2        -1
#           0        1        2         3         4
names = ["kenny", "james", "walter", "john", "jerry"]
print("\n")
print(names)

print("\n")
print(names[1])

print("\n")
print(names[:4]) # slice method in python list
print(names[:2])

print("\n")
print(names[-2])

print("\n")
names.insert(1, "jane")
print(names)

names.remove("john")
print(names)

print("\n")
numbers = [4, 3, 9, 2, 7, 8, 6, 10, 5]
numbers.sort()
print(numbers)

# =================LOOPS =================
# FOR LOOPS =================
# for each in every
for name in names:
    print(name)

print("\n")
for a in range(1, 11):
    print(a)

print("\n")

# whille loop 
x = 1 # floor figure
while x <= 20: # celiing figure
    print(x)
    x += 1   # incrementor plus 1

print("\n")
y = 2
while y <= 20: 
    print(y)
    y += 2 # incrementor plus 2

print("\n")

# combination of while loop and for loop
sn = 1
while sn <= len(names):
    for name in names:
        print(sn, end=".")
        sn += 1 # incrementor plus 1
        print(name)

# ======= Python Dictionary =================

kenny = {
    "Name": "Kenny",
    "Genders": "Male",
    "Age": "15yrs",
    "class": "SS2",
    "state": "Lagos",
    "Hobbies": "Reading",
}

jane = {
    "Name": "jane",
    "Genders": "Female",
    "Age": "16yrs",
    "class": "SS2",
    "state": "oyo",
        "Hobbies": "Music",

}

print(kenny)
print("\n")
print(jane)

print("\n")
print(kenny['Age'])

print("\n")
print(jane['state'])

print("\n")
get_keys =kenny.keys()
print(get_keys)

print("\n")
get_values = kenny.values()
print(get_values)

print("\n")
for ken in kenny.values():
    print(ken)

print("\n")
for keys, values in kenny.items():
    print(keys, ":" + str(values))
