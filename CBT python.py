from math import * # sqrt pow + - * /
from datetime import datetime, date
import calendar
import pytz # python time zone 
import random


# ========== How to build CBT with python class and object

class Examination:
    def __init__(self, single_question, single_answer):
        self.single_question = single_question
        self.single_answer = single_answer
exam_questions = [
    "1. What is the capital of Lagos state?\n (a) Ikeja \n (b) Ibadan \n (c) Oshogbo \n (d) Abeokuta \n", # 0
    "2. What is the capital of Osun state?\n (a) Ikeja \n (b) Ibadan \n (c) Oshogbo \n (d) Abeokuta \n", # 1
    "3. What is the capital of Oyo state?\n (a) Ikeja \n (b) Ibadan \n (c) Oshogbo \n (d) Abeokuta \n",  # 2
    "4. What is the capital of Ogun state?\n (a) Ikeja \n (b) Ibadan \n (c) Oshogbo \n (d) Abeokuta \n", # 3
]

# Examination.single_question
students = [
    Examination(exam_questions[0], 'a'), # 0
    Examination(exam_questions[1], 'c'), # 1
    Examination(exam_questions[2], 'b'), # 2
    Examination(exam_questions[3], 'd'), # 3
]


student_name = input("Enter your name: ")
print("\n")
score = 0

for student in students: # Destructure
    get_answer = input(str(student.single_question) + 'Ans: ')
    if get_answer == student.single_answer:
        score += 1

print(str(student_name) + " your score is: " + str(score) + "/4")
print( "Congratulations you passed the test")

print("\n")