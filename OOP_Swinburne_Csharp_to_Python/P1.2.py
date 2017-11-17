"""
    Author: vietnguyenswin (Viet Nguyen)
    Name: Pass task 1.2P
    Description: + Object-Oriented Programming with Python programming language.
                 + This is a rework version of required tasks for Object-Oriented Programming with C# unit
                    (COS20007 - Swinburne Semester 2 2016).
                 + The author understands the principles of Object-Oriented Analysis & Design and achieved Distinction
                    grade (COS20007).
                 + The motivation for doing this version is to practice using Python.
                 + The works of this version are public. Nevertheless, you should not copy & paste without understanding
                    the mechanisms behind.
    Instruction: + Compile the code then run to see the result.
    Last modified: 18 Nov 2017
"""


class Counter(object):
    def __init__(self, name):
        self.__name = name
        self.__count = 0

    def increment(self):
        self.__count += 1

    def reset(self):
        self.__count = 0

    # accessor (get) property
    @property
    def value(self):
        return self.__count

    @property
    def name(self):
        return self.__name

    # mutator (set) property
    @name.setter
    def name(self, name):
        self.__name = name


class Main(Counter):
    # static method. (notice that there is no "self")
    @staticmethod
    def printing(counters):
        # similar to foreach loop
        for c in counters:
            # string format with Python
            print("{0} is {1}".format(c.name, c.value))

    @staticmethod
    def act():
        # create a list with length = 3
        my_counters = [Counter] * 3
        # create new instances of Counter object
        my_counters[0] = Counter("Counter 1")
        my_counters[1] = Counter("Counter 2")
        my_counters[2] = my_counters[0]
        # for loop
        for i in range(0, 4):
            # call the method
            my_counters[0].increment()

        for i in range(0, 9):
            my_counters[1].increment()

        Main.printing(my_counters)
        my_counters[2].reset()
        Main.printing(my_counters)

Main.act()
