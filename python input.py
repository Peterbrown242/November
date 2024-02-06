from math import * # sqrt pow + - * /
from datetime import datetime, date
import calendar
import pytz # python time zone 
import random



# ======= Python Input ======
get_value = input("get_value: ")
print("your name is " + str(get_value))

# If statement wit python input
print("\n")
get_day = input("Enter day here: ")
if get_day == "monday":
    print("monday is meeting")
elif get_day == "tuesday":
    print("tuesday is purchase")
elif get_day == "wednesday":
    print("wednesday is training")
elif get_day == "thursday":
    print("thursday is safety measures")
elif get_day == "friday":
    print("friday is staff meetting")
elif get_day == "saturday":
    print("saturday is offday")
elif get_day == "sunday":
    print("sunday is offday")
else:
    print(str(get_day)+" is not a valid day of the week")