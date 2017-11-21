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

# define Identifiable class
class Identifiable(object):
    # constructor adds identifiers to the Identifiable object from the passed list
    def __init__(self, idents):
        self.__identifiers = list(idents)

    # check if the passed in identifier is in the __identifiers
    def are_you(self, id):
        if id in self.__identifiers:
            return True
            # print("oh yeah")
        else:
            return False
            # print("oh no")

    # return the first identifier in __identifiers
    @property
    def first_id(self):
        return self.__identifiers[0]

    # convert the identifier to lowercase and add it to __identifiers list
    def add_identifier(self, new_id):
        self.__identifiers.append(str(new_id).lower())


test = Identifiable(["hello", "hi"])
test.add_identifier("ajinomoto")
test.are_you("ajinomoto")
print test.first_id
