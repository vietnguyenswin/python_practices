import turtle
wn = turtle.Screen()

tess = turtle.Turtle()

def draw(x, y): # x, y are mouse position arguments passed by onclick()

    tess.clear() # Clear out the drawing (if any)
    tess.reset() # Reset the turtle to original position
    tess.hideturtle()

    tess.left(36)
    tess.forward(100)
    for a in range(4):
        tess.left(144)
        tess.forward(100)
    tess.right(36) # to go to original place

draw(0, 0) # Draw the first time

wn.onclick(draw) # Register function draw to the event mouse_click
wn.onkey(wn.bye, "q") # Register function exit to event key_press "q"

wn.listen() # Begin listening to events like key_press & mouse_clicks
wn.mainloop()