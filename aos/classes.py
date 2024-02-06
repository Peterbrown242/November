from math import * # sqrt pow + - * /
from datetime import datetime, date
import calendar
import pytz # python time zone 
import random

# A class is like a blueprint for creating objects. An object has properties and methods (functions) associated with it. 
# Almost everything in python is an object. 

# create class 

class Job:
    #Constructor
    def __init__(self, name, title, age,):
        self.name = name
        self.title = title
        self.age = age
        

    def greeting(self):
        return f'My name is {self.name} and i am {self.age}, my Job is a {self.title}'
    
    def has_birthday(self):
        self.age += 1

peter = Job('Peter', 'Web Developer', 25)

# Extend class

class Customer(Job):
    #Constructor 
    def __init__(self, name, title, age,): 
        self.name = name
        self.title = title
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and i am {self.age}, my Job is a {self.title} and my balance is {self.balance}'

    
# Initialize user object
Emmanuel = Customer('Emmanuel peter', 'Cyber Security', 24)

Emmanuel.set_balance(200)
print(Emmanuel.greeting())

# Initialize user object
peter.has_birthday()
print(peter.greeting())
# print(f'My name is {peter.name} and i am  {peter.age} years old. who is a {peter.title}')
        
import random

class Job:
    def __init__(self, name, title, age):
        self.name = name
        self.title = title
        self.age = age
        self.account_number = random.randint(1000000, 9999999)

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} years old, and my account number is {self.account_number}.'

# Initialize user object
john = Job('john', 'Web Developer', 25)
print(john.greeting())



