"""
    Author: vietnguyenswin (Viet Nguyen)
    Name: Pass task 1.1P
    Description: + Object-Oriented Programming with Python programming language.
                 + This is a rework version of required tasks for Object-Oriented Programming with C# unit
                    (COS20007 - Swinburne Semester 2 2016).
                 + The author understands the principles of Object-Oriented Analysis & Design and achieved Distinction
                    grade (COS20007).
                 + The motivation for doing this version is to practice using Python.
                 + The works of this version are public. Nevertheless, you should not copy & paste without understanding
                    the mechanisms behind.
    Instruction: + Type "Viet" --> the terminal will display "Welcome back my friend!" message.
                 + Type "Fred" --> the terminal will display "What a lovely name" message.
                 + Type "Wilma" --> the terminal will display "Great name" message.
                 + Other names will get "Beautiful name" message response.
                 + No case-sensitive.
    Last modified: 17 Nov 2017
"""


# Define Message class
# Without class --> There will be no object.
class Message(object):
    # Define a constructor of Message class
    def __init__(self, msg):
        # __msg means this is a private attribute
        self.__msg = msg

    # Define an implementation of Message class
    # This is a public method. Thus, it will be a part of the interface.
    # Other classes will able to use this method.
    def prt(self):
        print(self.__msg)


# Define Main class. This class uses the method in Message class
class Main(Message):
    # Create instances of Message object
    hello_world = Message("Hello World!")
    # Print it
    hello_world.prt()
    # Define response messages
    msg1 = "Welcome back my friend!"
    msg2 = "What a lovely name"
    msg3 = "Great name"
    msg4 = "Beautiful name"
    # Assign the messages to Python list
    messages = [msg1, msg2, msg3, msg4]
    # Iteration - infinity loop
    while True:
        # Ask for user's input
        name = raw_input("Enter name: ")
        # Control flow with if-else condition
        # lower() converts raw input to under case format
        if name.lower() == "viet":
            print(messages[0])
        elif name.lower() == "fred":
            print(messages[1])
        elif name.lower() == "wilma":
            print(messages[2])
        else:
            print(messages[3])
