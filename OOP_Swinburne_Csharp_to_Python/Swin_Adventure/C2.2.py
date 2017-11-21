"""
    Author: vietnguyenswin (Viet Nguyen)
    Name: Pass task 2.2C
    Description: + Object-Oriented Programming with Python programming language.
                 + This is a rework version of required tasks for Object-Oriented Programming with C# unit
                    (COS20007 - Swinburne Semester 2 2016).
                 + The author understands the principles of Object-Oriented Analysis & Design and achieved Distinction
                    grade (COS20007).
                 + The motivation for doing this version is to practice using Python.
                 + The works of this version are public. Nevertheless, you should not copy & paste without understanding
                    the mechanisms behind.
    Instruction: + Update later
    Last modified: 21 Nov 2017
"""


class Identifiable(object):
    def __init__(self, idents):
        self.__identifiers = list(idents)

    def are_you(self, id):
        if id in self.__identifiers:
            # return True
            print("oh yeah")
        else:
            # return False
            print("oh no")


test = Identifiable(["hello", "hi"])
test.are_you("hello")
