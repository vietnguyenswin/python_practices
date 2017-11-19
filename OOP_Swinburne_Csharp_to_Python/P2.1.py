from turtle import *


class Draw(object):
    @staticmethod
    def fill_rectangle(color, x, y, height, width):
        t = Turtle()
        screen = Screen()
        t.hideturtle()
        t.speed(0)
        t.color(color)
        t.up()
        t.goto(x, y)
        t.down()
        t.begin_fill()
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.end_fill()
        t.fillcolor(color)
        screen.exitonclick()


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
    def color(self, color):
        self.__color = color

    @color.getter
    def color(self):
        return self.__color

    # x property
    @property
    def x(self, x):
        self.__x = x

    @x.getter
    def x(self):
        return self.__x

    # y property
    @property
    def y(self, y):
        self.__y = y

    @y.getter
    def y(self):
        return self.__y

    # width property
    @property
    def width(self, width):
        self.__width = width

    @x.getter
    def width(self):
        return self.__width

    # height property
    @property
    def height(self, height):
        self.__height = height

    @y.getter
    def height(self):
        return self.__height

    def draw(self):
        Draw.fill_rectangle(self.__color, self.__x, self.__y, self.__height, self.__width)


class Main(Shape, ):
    @staticmethod
    def action():
        my_shape = Shape()
        my_shape.draw()

Main.action()
