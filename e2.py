"""
    Author: vietnguyenswin
    Name: Exercise 2
    Description: String processing with Python
    Last modified: 16 Nov 2017
"""


def input_string():
    return raw_input("Please submit the string: ")


def string_process():
    # Assigning value for a variable
    s = input_string()
    if s.isalpha():
        print "input is alpha characters"
    elif s.isdigit():
        print "input is digit characters"
    # Converting from list to tuple
    tuples = tuple(list(s))
    print tuples


while True:
    string_process()