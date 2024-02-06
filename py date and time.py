from datetime import datetime, date
import calendar
import pytz # python time zone 
import random


# ======== PHYTON DATE AND TIME =================
today = date.today()

format1 = today.strftime("%Y-%m-%d")
print(format1)

print("\n")

formart2 = today.strftime("%d %b %y (%a) ")
print(formart2)

print("\n")

format3 = today.strftime("%D %B %Y (%A) ")
print(format3)

print("\n")

format4 = today.strftime("%H:%M:%S ")
print(format4)

print("\n")

format5 = today.strftime("%I:%M:%p")
print(format5)
print("\n")

format6 = today.strftime("%H:%M")
print(format6)
print("\n")