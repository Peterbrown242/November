from math import * # sqrt pow + - * /
from datetime import datetime, date
import calendar
import pytz # python time zone 
import random


# CBT JAMB ASSIGNMENT 



print("INSTRUCTIONS:")
print("\n")

print(" This test consist of 20 questions related to ICT. Your scores will be automatic generated.")
print("\n")

print(" *All questions must be answered* ")
print("\n")
print(f'Time', 20 ,'Minutes')

from datetime import datetime

import time




while True:
    now = datetime.now()
    format4 = now.strftime("%H:%M:%S ")

    

    print(format4, end='\r')
    time.sleep(1)

    # print("\n")
    # # now = datetime.now()
    # today = date.today()
    # format_datetime = today.strftime("%D %B %Y (%A) ")
    # print(format_datetime)
    # print("\n")


    class Examination:
        def __init__(self, single_question, single_answer):
            self.single_question = single_question
            self.single_answer = single_answer
    exam_questions = [
        "1. _________ controls the way in which the computer system functions and provides a means by which users can interact with the computers?\n (a) Operating System \n (b) System Server \n (c) Motherboard \n", # 0
        "2. The difference between people with access to computers and the internet and those without this access is known as _______.?\n (a) Internet divide \n (b) Web divide \n (c) Digital divide \n", # 1
        "3. Server are computers that provide resources to other computer connected to a _______.\n (a) Mainframe \n (b) Network \n (c) Client \n", # 2
        "4. Word processing, spreadsheet, and photo-editing are examples of _______.\n (a) System Software \n (b) Application Software \n (c) Operating System Software \n", # 3
        "5. __________ is used to update drivers in the control panel.\n (a) Device Manager \n (b) Profile Manager \n (c) System Manager \n", # 4
        "6. All of the following are examples of input devices EXCEPT __________.\n (a) Mouse \n (b) Keyboard \n (c) Printer \n", # 5
        "7. Which of the following is a standard unit for measuring digital file size.\n (a) Bytes \n (b) Length \n (c) Metre \n", # 6
        "8. In the binary language each letter of the alphabet, each number and each special character is made up of a unique combination of ______.\n (a) Eight Bytes \n (b) Eight Bits \n (c) Eight Kilobytes \n", # 7
        "9. _______ is data that has been organized or presented in a meaningful way.\n (a) Storage \n (b) Information \n (c) Software \n", # 8
        "10. All of the following are examples of real security and privacy risk EXCEPT _________.\n (a) Hackers \n (b) Spam \n (c) Viruses \n", #9
        "11. _______ is the place used to store all system files and user information in a computer \n (a) none of the above \n (b) Folders \n (c) Files \n ", # 10
        "12. The set of instructions that tells the computer what to do is ______.\n (a) Database \n (b) Software \n (c) Hardware \n ", # 11
        "13. Which of the following stores more data ? \n (a) DVD \n (b) CD ROM \n (c) ROM \n (d) CD RW \n", # 12
        "14. ______ is the heart of the computer and this is where all the computing is done \n (a) Output device \n (b) Input device \n (c) CPU \n", # 13
        "15. The unit of bytes in megabytes is what \n (a) 1,078,776 bytes \n (b) 1,055,986 bytes \n (c) 1048,576 bytes \n ", #14
        "16. To all move forward through tabs \n (a) CTRL + SHIFT + TABS \n (b) CTRL + TABS \n (c) SHIFT + TABS \n ", #15
        "17. A text/image clicked to link to another page in a website is called _________ \n (a) New window \n (b) New tab \n (c) Hyperlink \n ", #16
        "18. The shortcut required to cut a part of a file and paste it in another location is called _________ \n (a) Ctrl+X. / Ctrl+V. \n (b) Ctrl+Z. / Ctrl+Y. \n (c) ctrl+S. / Ctrl+H. \n ", #17
        "19. _______ is a place for storing temporary deleted files \n (a) Desktop \n (b) Recycle bin \n (c) Storage \n ", #18
        "20. The operating system is the _______ on a computer \n (a) Software Program \n (b) Computer Program \n (c) Network Program \n ", #19



    ]



    students = [
        Examination(exam_questions[0], 'a'), # 0
        Examination(exam_questions[1], 'c'), # 1
        Examination(exam_questions[2], 'b'), # 2
        Examination(exam_questions[3], 'b'), # 3
        Examination(exam_questions[4], 'a'), # 4
        Examination(exam_questions[5], 'c'), # 5
        Examination(exam_questions[6], 'a'), # 6
        Examination(exam_questions[7], 'b'), # 7
        Examination(exam_questions[8], 'b'), # 8
        Examination(exam_questions[9], 'b'), # 9
        Examination(exam_questions[10], 'c'), # 10
        Examination(exam_questions[11], 'b'), # 11
        Examination(exam_questions[12], 'a'), # 12
        Examination(exam_questions[13], 'c'), # 13
        Examination(exam_questions[14], 'c'), # 14
        Examination(exam_questions[15], 'c'), # 15
        Examination(exam_questions[16], 'c'), # 16
        Examination(exam_questions[17], 'a'), # 17
        Examination(exam_questions[18], 'b'), # 18
        Examination(exam_questions[19], 'a'), # 19


    

    ]


    student = {
        ' Full_name': input('Enter your Full name:'),
        'Age': input('Enter your Age:'),
        'class': input('Enter your Class:'),
        'Department': input('Enter your Department:'),
    }
    
    print("\n")
    score = 0

    for student in students:
        get_answer = input(str(student.single_question) + 'Ans: ')
    if get_answer == student.single_answer:
        score += 1

    print(str(student) + " your score is: " + str(score) + "/20")
    if score >= 10 :
        print("Congratulations you passed the test")
    else:
        print("You did not pass the test")

    print("\n") 