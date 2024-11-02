import turtle
turt = turtle.Turtle()

turt.speed(10)

for i in range(90):

    turt.pendown()
    turt.forward(100)
    turt.right(10)
    turt.forward(100)
    turt.setposition(0,0)

turt.pendown()
turtle.done()
