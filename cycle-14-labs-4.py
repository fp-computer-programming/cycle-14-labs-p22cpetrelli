#author CJP 03/24/2022
#import turtle
import turtle

#creates window
window = turtle.Screen()
window.setup()
window.title("Lab 4")
#gives turtle a name and color
drake = turtle.Turtle()
drake.speed(3)
drake.shape("turtle")
drake.pencolor("orange")
drake.fillcolor("blue")

#speed and direction
drake.stamp()
drake.speed(10)
drake.penup()
drake.setposition(100,100)

#moves turtle
drake.pendown()
drake.goto(200,100)
drake.goto(200,0)
drake.goto(100,0)
drake.goto(100,100)

#window stays open
window.mainloop()