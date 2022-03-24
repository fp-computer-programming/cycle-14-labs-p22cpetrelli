#author CJP 03/24/2022
# import turtles plugin
import turtle

# defines rotations and movement function
def move_forward():
    ted.forward(50)

def move_backward():
    ted.backward(50)

def turn_left():
    ted.left(90)

def turn_right():
    ted.right(90)

# creates the window
window = turtle.Screen()

# creates the turtle
ted = turtle.Turtle()

# makes movements to keys
window.onkey(move_forward, "Up")
window.onkey(move_backward, "Down")
window.onkey(turn_left, "Left")
window.onkey(turn_right, "Right")

#window stays open
window.listen()
window.mainloop()