#author CJP 03/24/2022
#import turtle
import turtle 

#creates window
window = turtle.Screen()
window.setup(500, 500)
window.screensize(100,100)
window.title("Lab 2")

#sets the name of turtle
ted = turtle.Turtle()

#moves turtle
ted.forward(100)
ted.right(120)
ted.forward(100)
ted.right(120)
ted.forward(100)

#window stays open
window.mainloop()