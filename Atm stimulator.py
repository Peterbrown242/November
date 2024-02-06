from math import * # sqrt pow + - * /
from datetime import datetime, date
import calendar
import pytz # python time zone 
import random







# ============== Atm Machine Simulator==============
bank_balance = 5000
withdraw = int(input("Enter amount to withdraw: "))
if withdraw > bank_balance:
    print("Insyfficient funds. Your balance is " + str(bank_balance))
else:
    new_balance = bank_balance - withdraw
    print("You have successfully withdraw " + str(withdraw) + "Your current balance" + str(new_balance))


print("\n")

bank_balance = 3000
withdraw = int(input("Enter amount to withdraw:"))
if withdraw > bank_balance:
    print("Insufficient funds. Your balance is " + str(bank_balance))
else:
    new_balance = bank_balance - withdraw
    print("you have a successful withdraw" + str(withdraw) + "your current balance" + str(new_balance))

