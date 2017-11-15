"""
    Author: vietnguyenswin
    Name: Exercise 1 OO
    Description: Getting started using Python (Object-Oriented)
    Last modified: 16 Nov 2017
"""


# basic Python syntax
# Python class
# Class Activity
class Activity(object):
    # Using static method as the way to create new instance of Activity class is unusual
    # Using @staticmethod decorator
    @staticmethod
    def validator():
        a = raw_input("Please provide an integer: ")
        if a == "":
            return "Please fill the input!"
        elif not a.isdigit(): # Validate input
            return "Please check the input!"
        else:
            # Formatting string
            return "Your submitted result is: {0:s}".format(a)


# Class Main
class Main(Activity):
    # Again, using static method
    @staticmethod
    def calling():
        # Infinity loop
        while True:
            # Printing out the returns
            print Activity.validator()

Main.calling()
