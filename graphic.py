"""
    Author: vietnguyenswin
    Description: Simple graphic handling with Python - turtle module
    Last modified: 16 Nov 2017
"""
# Import turtle module
import turtle

# Create an instance of the imported module
grap = turtle.Turtle()
# Make a screen
scrn = turtle.Screen()
# Define a function
def graphic_control():
    # Draw a line
    grap.forward(150)
    # Finish
    turtle.done()
# Call the function
graphic_control()
