from math import * # sqrt pow + - * /
from datetime import datetime, date
import calendar
import pytz # python time zone 
import random






# ============ Random Function =================
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

import random

top_number = input("Type a number:")


if top_number.isdigit():
    top_number = int(top_number)

    if top_number <= 0:
        print('Please type a number larger than 0')
        quit()
else:
    print('Please type a number next time')
    quit()

random_number = random.randint(0, top_number)
guesses = 0
print(random_number)

while True: 
    guesses += 1  # means everything is true,   # break means to stop the loop.. 
    user_guess = input("Make a guess:")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('type a number next time')
        continue   # means brings back to the top means start again..

    if user_guess == random_number: # means everything
        print('you got it')
        break
    else:
        print('you got it wrong')

print("you got it in", guesses, "guesses")



