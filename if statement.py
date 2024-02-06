from math import * # sqrt pow + - * /
from datetime import datetime, date
import calendar
import pytz # python time zone 
import random


#====================IF STATEMENT ===============
if 2 > 5:
    print("This is unbelieveable.")
else:
    print("There is no way 2 can be greater than 5") 

# Nested if statement ========

print("\n")
my_today = "thursday"

if my_today == "monday":
    print("monday is workday")
elif my_today == "tuesday":
    print("tuesday is workday")
elif my_today == "wednesday":
    print("wednesday is workday")
elif my_today == "thursday":
    print("thursday is workday")
elif my_today == "friday":
    print("friday is workday")
elif my_today == "saturday":
    print("saturday is offday")
elif my_today == "sunday":
    print("sunday is offday")
else:
    print(str(my_today)+" is not a valid day of the week")

print("\n")
