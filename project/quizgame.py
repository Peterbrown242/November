from math import * # sqrt pow + - * /
from datetime import datetime, date
import calendar
import pytz # python time zone 
import random

# ROCK, PAPER AND SCISSORS


user_wins = 0
computer_wins = 0

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in ["rock", "paper", "scissors"]:
        continue

    random_number = random.randint(0, 2)
    # rock : 0, paper : 1, scissors : 2   

print("Goodbye!")



# PASSWORD MANAGER 

