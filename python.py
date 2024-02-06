from math import * # sqrt pow + - * /
from datetime import datetime, date
import calendar
import pytz # python time zone 
import random




# This is a comment in python. Generally for developer notes

#Date Types

#1. String Data
name = "james"
print(name)

print("\n") # spacing btw 2 output
#2. Integer Data
my_number = 256
print(my_number)

print("\n")
#3. Float Data (decimal num)
my_float = 3.142
print(my_float)

print("\n")
#4. Boolean Data (True or False)
yes = True
print(yes)

print("\n")
#=========PYTON OPERATORS =================================
#(+ - * / )
y = 5
x = 3

z1 = y + x 
print(z1)

print("\n")

z2 = y - x
print(z2)

print("\n")

z3 = y * x
print(z3)

print("\n")

z4 = y / x
print(z4)

print("\n")

# #==========Math Properties ============
# my_sqrt = sqrt(144)
# print(my_sqrt)

# print("\n")
# my_exponential = pow(2, 5)
# print(my_exponential)

# print("\n")

# my_numbers = max(2, 8, 7, 3, 9, 1, 5)
# print(my_numbers)

# print("\n")
# my_numbers = min(2, 8, 7, 3, 9, 1, 5)
# print(my_numbers)

# print("\n")

# value = 2.4
# ceil_value = ceil(value)
# print(ceil_value)

# print("\n")

# floor_value = floor(value)
# print(floor_value)

# print("\n")

# approximate = round(z4, 2)
# print(approximate)

# #====================IF STATEMENT ===============
# if 2 > 5:
#     print("This is unbelieveable.")
# else:
#     print("There is no way 2 can be greater than 5") 

# # Nested if statement ========

# print("\n")
# my_today = "thursday"

# if my_today == "monday":
#     print("monday is workday")
# elif my_today == "tuesday":
#     print("tuesday is workday")
# elif my_today == "wednesday":
#     print("wednesday is workday")
# elif my_today == "thursday":
#     print("thursday is workday")
# elif my_today == "friday":
#     print("friday is workday")
# elif my_today == "saturday":
#     print("saturday is offday")
# elif my_today == "sunday":
#     print("sunday is offday")
# else:
#     print(str(my_today)+" is not a valid day of the week")

# print("\n")

# # ======= Python Input ======
# get_value = input("get_value: ")
# print("your name is " + str(get_value))

# # If statement wit python input
# print("\n")
# get_day = input("Enter day here: ")
# if get_day == "monday":
#     print("monday is meeting")
# elif get_day == "tuesday":
#     print("tuesday is purchase")
# elif get_day == "wednesday":
#     print("wednesday is training")
# elif get_day == "thursday":
#     print("thursday is safety measures")
# elif get_day == "friday":
#     print("friday is staff meetting")
# elif get_day == "saturday":
#     print("saturday is offday")
# elif get_day == "sunday":
#     print("sunday is offday")
# else:
#     print(str(get_day)+" is not a valid day of the week")

#  #============== PHYTHON CALCULATOR =============================
# first_num = int(input("Enter first number:"))
# operator = input("Enter operator: ")
# second_num = int(input("Enter second number:"))

# if operator == "+":
#     answer = first_num + second_num
# elif operator == "-":
#     answer = first_num - second_num
# elif operator == "*":
#     answer = first_num * second_num
# elif operator == "/":
#     answer = first_num / second_num
#     answer = round(answer, 2)
# else:
#     answer = "syntax error"

# print(answer)           

# # ============== Atm Machine Simulator==============
# bank_balance = 5000
# withdraw = int(input("Enter amount to withdraw: "))
# if withdraw > bank_balance:
#     print("Insyfficient funds. Your balance is " + str(bank_balance))
# else:
#     new_balance = bank_balance - withdraw
#     print("You have successfully withdraw " + str(withdraw) + "Your current balance" + str(new_balance))

# # ============ Random Function =================
# rand_four = random.randint(1000, 9999)
# print(rand_four)

# rand_seven = random.randint(1000000, 9999999)
# rand_seven1 = random.randint(1000000, 9999999)
# branch_code = "231"
# account_number = str(branch_code) + str(rand_seven)
# account_number2 = str(branch_code) + str(rand_seven1)
# print("\n")
# print(account_number)
# print(account_number2)
# print("\n")

# #------Python List -------(Storage of multiples values in a single variable)
# #           -5       -4       -3        -2        -1
# #           0        1        2         3         4
# names = ["kenny", "james", "walter", "john", "jerry"]
# print("\n")
# print(names)

# print("\n")
# print(names[1])

# print("\n")
# print(names[:4]) # slice method in python list
# print(names[:2])

# print("\n")
# print(names[-2])

# print("\n")
# names.insert(1, "jane")
# print(names)

# names.remove("john")
# print(names)

# print("\n")
# numbers = [4, 3, 9, 2, 7, 8, 6, 10, 5]
# numbers.sort()
# print(numbers)

# # =================LOOPS =================
# # FOR LOOPS =================
# # for each in every
# for name in names:
#     print(name)

# print("\n")
# for a in range(1, 11):
#     print(a)

# print("\n")

# # whille loop 
# x = 1 # floor figure
# while x <= 20: # celiing figure
#     print(x)
#     x += 1   # incrementor plus 1

# print("\n")
# y = 2
# while y <= 20: 
#     print(y)
#     y += 2 # incrementor plus 2

# print("\n")

# # combination of while loop and for loop
# sn = 1
# while sn <= len(names):
#     for name in names:
#         print(sn, end=".")
#         sn += 1 # incrementor plus 1
#         print(name)

# # ======= Python Dictionary =================

# kenny = {
#     "Name": "Kenny",
#     "Genders": "Male",
#     "Age": "15yrs",
#     "class": "SS2",
#     "state": "Lagos",
#     "Hobbies": "Reading",
# }

# jane = {
#     "Name": "jane",
#     "Genders": "Female",
#     "Age": "16yrs",
#     "class": "SS2",
#     "state": "oyo",
#         "Hobbies": "Music",

# }

# print(kenny)
# print("\n")
# print(jane)

# print("\n")
# print(kenny['Age'])

# print("\n")
# print(jane['state'])

# print("\n")
# get_keys =kenny.keys()
# print(get_keys)

# print("\n")
# get_values = kenny.values()
# print(get_values)

# print("\n")
# for ken in kenny.values():
#     print(ken)

# print("\n")
# for keys, values in kenny.items():
#     print(keys, ":" + str(values))


# # User Defined FUnctions 
# def area_of_rectangle(lenght, breadth):
#     aor = int(lenght) * int(breadth)
#     print(str(aor) + "m²")

# length = input('Enter Lenght:')
# breadth = input('Enter Breadth:')
# area_of_rectangle(length, breadth)

# print("\n")

# def area_of_square(l):
#     aos = int(l) * int(l)
#     print(str(aos) + "m³")

# l = input('Enter square lenght: ')
# area_of_square(l)

# print("\n")
py = 3.142

def area_of_circle(radius):
    py = 3.142
    area_of_circle =  py * int(radius) * int(radius) 
    print("Area of circle is " + str(area_of_circle) )


radius = int(input("Enter radius:"))
area_of_circle(radius)

print("\n")

py = 3.1425

def area_of_cylinder(x, y):
    area_of_cylinder = py * int(radius) + int(height) / 7
    print(area_of_cylinder)

radius = input("Enter radius")
height = input("Enter height")
area_of_cylinder(radius, height) 


print("\n")






print("\n")

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


# OOP object oriented programing

# class: This refers to python groups and category
# object: refers to members of this class
# Attributes: are the characteristics of the object
# values: assigned to the attributes

class SS2:
    def __init__(self, name, gender, age, department, state):
        self.name = name
        self.gender = gender
        self.age = age
        self.state = state
        self.department = department


james = SS2("james", "Male", "17", "Science", "Osun state")
Serah = SS2("serah", "Male", "18", "commercial", " Lagos state")

print("\n")
print("james")

print("\n")

# LETS BUILD A FOOD TIMETABLE WITH CLASS AND OBJECTS
class Food_timetable:
    def __init__(self, breakfast, lunch, dinner):
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner


Monday = Food_timetable("chicken & chips", "fried rice", "dodo / egg / fried potatoe")
Tuesday = Food_timetable("toast and tea", "jollof noodles", "fruit salad")
Wednesday = Food_timetable("pancake and coffee", "offada rice", "akara & pap")
Thursday = Food_timetable("coker oat & strawberry", "amala & igbegiri", "groundnut & cucumber")
Friday = Food_timetable("Spagetti & shrimp", "ijebu garri & groundnut", "semo & efforire")
Saturday = Food_timetable("Yam & eggo", "beans &  custard", "fish pepper soup")
Sunday = Food_timetable("Bread / sardine / egg", "Rice & chicken stew", "pizza")

print(Thursday.lunch)
print(Sunday.dinner)
print("\n")

all_mondays = ["chicken & chips", "fried rice", "dodo_egg_fried potatoe"]
print(all_mondays)
print("\n")
print(len(all_mondays))

i = 1
while i <= len(all_mondays):
    for all_monday in all_mondays:
        print(i, end=".")
        i += 1
        print(all_monday)

print("\n")

all_tuesdays = ["toast and tea", "jollof noodles", "fruit salad"]
print(all_tuesdays)
print("\n")
print(len(all_tuesdays))

i = 1
while i <= len(all_tuesdays):
    for all_tuesday in all_tuesdays:
        print(i, end=".")
        i += 1
        print(all_tuesday)
        
