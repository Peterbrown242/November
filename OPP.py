from datetime import datetime, date
import calendar
import pytz # python time zone 
import random


# OOP object oriented programing

# main body of OOP listed below
#              ⬇
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
# class Food_timetable:
#     def __init__(self, breakfast, lunch, dinner):
#         self.breakfast = breakfast
#         self.lunch = lunch
#         self.dinner = dinner


# Monday = Food_timetable("chicken & chips", "fried rice", "dodo / egg / fried potatoe")
# Tuesday = Food_timetable("toast and tea", "jollof noodles", "fruit salad")
# Wednesday = Food_timetable("pancake and coffee", "offada rice", "akara & pap")
# Thursday = Food_timetable("coker oat & strawberry", "amala & igbegiri", "groundnut & cucumber")
# Friday = Food_timetable("Spagetti & shrimp", "ijebu garri & groundnut", "semo & efforire")
# Saturday = Food_timetable("Yam & eggo", "beans &  custard", "fish pepper soup")
# Sunday = Food_timetable("Bread / sardine / egg", "Rice & chicken stew", "pizza")

# print(Thursday.lunch)
# print(Sunday.dinner)
# print("\n")

# all_mondays = ["chicken & chips", "fried rice", "dodo_egg_fried potatoe"]
# print(all_mondays)
# print("\n")
# print(len(all_mondays))

# i = 1
# while i <= len(all_mondays):
#     for all_monday in all_mondays:
#         print(i, end=".")
#         i += 1
#         print(all_monday)

# print("\n")

# all_tuesdays = ["toast and tea", "jollof noodles", "fruit salad"]
# print(all_tuesdays)
# print("\n")
# print(len(all_tuesdays))

# i = 1
# while i <= len(all_tuesdays):
#     for all_tuesday in all_tuesdays:
#         print(i, end=".")
#         i += 1
#         print(all_tuesday)
