from datetime import datetime, date
import calendar
import pytz # python time zone 
import random



def dollar_to_naira(dollar):
    naira =  1230 * int(dollar)
    print('₦' + str(naira))

dollar = input("Enter dollar amount: ")
dollar_to_naira(dollar)

print("\n")

def naira_to_dollar(naira):
    dollar =  int(naira) / 1230
    print("$" + str(dollar))

naira = input("Enter naira amount: ")
naira_to_dollar(naira)

print("\n")

def euro_to_naira(euro):
    naira = 1650 * int(euro)
    print('₦' + str(naira))

euro = input("Enter euro amount: ")
euro_to_naira(euro)