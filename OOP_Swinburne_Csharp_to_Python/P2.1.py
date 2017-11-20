"""
    Author: vietnguyenswin (Viet Nguyen)
    Name: Pass task 2.1P
    Description: + Object-Oriented Programming with Python programming language.
                 + This is a rework version of required tasks for Object-Oriented Programming with C# unit
                    (COS20007 - Swinburne Semester 2 2016).
                 + The author understands the principles of Object-Oriented Analysis & Design and achieved Distinction
                    grade (COS20007).
                 + The motivation for doing this version is to practice using Python.
                 + The works of this version are public. Nevertheless, you should not copy & paste without understanding
                    the mechanisms behind.
    Instruction: + Use cd command to redirect the terminal working directory into the folder which you store this file.
                 + Execute this command: python P2.1.py
    Last modified: 20 Nov 2017
"""

# import turtle for graphical purpose with python
from turtle import *
# import random module to use random selection
import random


# Define Draw class
class Draw(object):
    # Define static method of fill_rectangle which will be call to draw a rectangle
    @staticmethod
    def fill_rectangle(color, x, y, height, width):
        t = Turtle()
        # create an instance of turtle
        # hide the arrow (turtle)
        t.hideturtle()
        # act as fast as it can
        t.speed(0)
        # color for the shape
        t.color(color)
        # start to fill the shape
        t.begin_fill()
        # ready to move the turtle
        t.up()
        # go to the location
        t.goto(x, y)
        # ready to draw
        t.down()
        # draw a rectangle
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        # stop to fill the shape
        t.end_fill()
        # fill the shape now
        t.fillcolor(color)


# Define Shape class
class Shape(Draw):
    # constructor
    def __init__(self):
        super(Shape, self).__init__()
        self.__x = 0
        self.__y = 0
        self.__width = 100
        self.__height = 100
        self.__color = "green"

    # color property
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    # x property
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    # y property
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    # width property
    @property
    def width(self):
        return self.__width

    # height property
    @property
    def height(self):
        return self.__height

    # define draw method
    def draw(self):
        Draw.fill_rectangle(self.__color, self.__x, self.__y, self.__height, self.__width)


# Define Main class
class Main(Shape):
    @staticmethod
    def action():
        # create new instance of Shape object
        my_shape = Shape()
        # Random assignments to new_x and new_y
        new_x = random.choice(tuple(range(-200, 200)))
        new_y = random.choice(tuple(range(-200, 200)))
        # Random color
        # colors tuple
        colors = ("blue", "black", "green", "orange", "red", "purple")
        # pick up one
        my_shape.color = random.choice(colors)
        # assign new_x & new_y to new shape
        my_shape.x = new_x
        my_shape.y = new_y
        # draw the shape
        my_shape.draw()
        # please don't close the window
        mainloop()


m = Main()
m.action()
