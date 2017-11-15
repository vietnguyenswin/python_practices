"""
    Author: vietnguyenswin
    Name: Exercise 1
    Description: Getting started using Python
    Last modified: 16 Nov 2017
"""


# basic Python syntax
# Python function
def int_type(a):
    # Condition check:
    if a == "":
        return "You must provide an integer!"
    # Check data type
    elif not a.isdigit():
        return "Please check you input!"
    else:
        # String format
        return "Your submitted result is: {0:s}".format(a)

# Control flow with while loop
# Input request
while True:
    # Print to the screen
    # Call a function
    print int_type(raw_input("\nEnter an integer: "))