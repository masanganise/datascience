# Python basics
# 1 Printing in new lines and using tabs
# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\t Like a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")

# 2 Write a Python program to find out what version of Python you are using
# import sys
# print("Python version")
# print(sys.version)
# print("Version info")
# print(sys.version_info)

# 3 Write a Python program to display the current date and time.
# import datetime
# now = datetime.datetime.now()
# print("Current date and time: ")
# print(now.strftime("%Y-%m-%d %H:%M:%S"))

# 4 Write a Python program that calculates the area of a circle based on the radius entered by the user.
# from math import pi
# r = float(input("Input the radius of the circle: "))
# area = pi * r ** 2
# print("The area of the circle with radius " +
#      str(r) + " is: " + str(round(area, 3)))

# 5 Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
# first_name = str(input("Enter first name:"))
# last_name = str(input("Enter last name: "))
# print(last_name + " " + first_name)
