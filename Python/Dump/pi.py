import turtle
from math import pi

turt = turtle.Turtle()

turt.speed(10)

for i in range(40):
    turt.pendown()
    turt.forward(100)
    turt.penup()
    turt.forward(10)
    turt.down()
    turt.circle(5)
    turt.penup()
    turt.right(10)
    turt.setposition(0, 0)

turt.pendown()
turtle.done()
