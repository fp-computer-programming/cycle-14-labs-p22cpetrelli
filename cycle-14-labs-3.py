#author CJP 03/24/2022
#import turtle
import turtle
#creates window
window = turtle.Screen()
window.setup(500, 500)
window.title("Lab 3")
window.bgcolor("tan")
#gives turtle name
ted = turtle.Turtle()
ted.shape("turtle")
ted.pencolor("blue")

#moves turtle
for x in range(3):
    ted.forward(200)
    ted.left(120)

#window stays opebn
window.mainloop()