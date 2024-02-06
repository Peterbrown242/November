from math import * # sqrt pow + - * /
from datetime import datetime, date
import calendar
import pytz # python time zone 
import random


def simple_interest(p, r, t):
     si = (int(p) * int(r) * int(t) ) / 100
     print("₦" + str(si))


p = input('Enter principal:')
r = input('Enter rate:')
t = input('Enter time:')
simple_interest(p, r, t)