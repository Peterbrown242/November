from datetime import datetime, date
import calendar
import pytz # python time zone 
import random



# User Defined FUnctions 
def area_of_rectangle(lenght, breadth):
    aor = int(lenght) * int(breadth)
    print(str(aor) + "m²")

length = input('Enter Lenght:')
breadth = input('Enter Breadth:')
area_of_rectangle(length, breadth)

print("\n")

def area_of_square(l):
    aos = int(l) * int(l)
    print(str(aos) + "m³")

l = input('Enter square lenght: ')
area_of_square(l)

print("\n")

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
    print("Area of cylinder is " + str(area_of_cylinder))

radius = input("Enter radius")
height = input("Enter height")
area_of_cylinder(radius, height) 


print("\n")