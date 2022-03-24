#author CJP 03/24/2022
#import turtles 
import turtle

#creates the window
window = turtle.Screen()

#creates the turtle
ted = turtle.Turtle()

#prompts the user to enter color and size of turtle
ted.color(window.textinput("Color?", "What color would you like?"))
size = int(window.textinput("Size?", "What size would you like the turtle to be (1-5)?"))

#creates size 
if size > 5:
    ted.shapesize(5)
elif size < 1:
    ted.shapesize(1)
else:
    ted.shapesize(size)

#moves turtle
ted.begin_fill()
ted.forward(100)
ted.right(90)
ted.forward(100)
ted.right(90)
ted.forward(100)
ted.right(90)
ted.forward(100)
ted.end_fill()

#window stays open
window.listen()
window.mainloop()