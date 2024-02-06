from math import * # sqrt pow + - * /
from datetime import datetime, date
import calendar
import pytz # python time zone 
import random


 #============== PHYTHON CALCULATOR =============================
first_num = int(input("Enter first number:"))
operator = input("Enter operator: ")
second_num = int(input("Enter second number:"))

if operator == "+":
    answer = first_num + second_num
elif operator == "-":
    answer = first_num - second_num
elif operator == "*":
    answer = first_num * second_num
elif operator == "/":
    answer = first_num / second_num
    answer = round(answer, 2)
else:
    answer = "syntax error"

print(answer)           