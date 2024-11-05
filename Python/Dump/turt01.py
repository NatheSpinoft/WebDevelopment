import turtle

pen = turtle.Turtle()

for i in range(480):
    x =+ 1
    y =+ 1
    pen.forward(x)
    pen.right(y)
    
    pen.left(50)
    for i in range(480):
        x =+ 1
        y =+ 1
        pen.forward(x)
        pen.right(y)
pen.pendown()
turtle.done
