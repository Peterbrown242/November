from math import * # sqrt pow + - * /
from datetime import datetime, date
import calendar
import pytz # python time zone 
import random

# JSON is commonly used with data APIS. Here is how we can parse JSON into python dictionary

import json

# Sample JSON
userJSON = '{"first_name": "john", "last_name": "Doe", "age": 30} '

# Parse to python dictionary
user = json.loads(userJSON)

print(user)
print(user["first_name"])

car = {'maker': 'ford', 'model': 'lexus', 'year': 2024}

carJSON = json.dumps(car)
print(carJSON)