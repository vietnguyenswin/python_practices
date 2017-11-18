"""
    Author: vietnguyenswin (Viet Nguyen)
    Name: Pass task 3.2P
    Description: + Object-Oriented Programming with Python programming language.
                 + This is a rework version of required tasks for Object-Oriented Programming with C# unit
                    (COS20007 - Swinburne Semester 2 2016).
                 + The author understands the principles of Object-Oriented Analysis & Design and achieved Distinction
                    grade (COS20007).
                 + The motivation for doing this version is to practice using Python.
                 + The works of this version are public. Nevertheless, you should not copy & paste without understanding
                    the mechanisms behind.
    Instruction: + Use cd command to redirect the terminal working directory into the folder which you store this file.
                 + Execute this command: python P3.2.py
    Last modified: 18 Nov 2017
"""

import time
import os


# Define Counter class for Counter object
class Counter(object):
    # new instance of Counter object will be assigned init value = 0 when created
    def __init__(self):
        self.__count = 0

    # public methods & they are parts of the class interface
    def tick(self):
        self.__count += 1

    def reset(self):
        self.__count = 0

    # property: getter | clock object will send message to Counter object to use this property
    @property
    def value(self):
        return self.__count


# Define Clock class
class Clock(Counter):
    def __init__(self):
        super(Clock, self).__init__()
        self.hour = Counter()
        self.minute = Counter()
        self.second = Counter()

    def __mechanism(self):
        # Tick the second just like the functional clock
        self.second.tick()
        # Hold on, wait for 1 second until another tick
        time.sleep(1)
        # if condition to control the tick
        if self.second.value >= 60:
            self.minute.tick()
            self.second.reset()
        if self.minute.value >= 60:
            self.hour.tick()
            self.minute.reset()
        if self.hour.value >= 24:
            self.hour.reset()

    def display(self):
        # infinity loop
        while True:
            # send message to the mechanism method
            self.__mechanism()
            # check if the current OS system is Windows or Mac
            # clear previous printed message before printing the new one
            if os.name != "nt":
                os.system("clear")
            else:
                os.system("cls")
            # print the clock
            # use format function | 0>2d: 5 --> 05
            print("{0:0>2d}:{1:0>2d}:{2:0>2d}".format(self.hour.value, self.minute.value, self.second.value))


# create an instance of the Clock object
clock = Clock()
# call the method
clock.display()
