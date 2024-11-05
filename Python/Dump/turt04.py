import turtle

screen = turtle.Screen()
screen.setworldcoordinates(-200, -200, 200, 200)

pen = turtle.Turtle()
pen.speed(3)

a = 0.6 #width
b = 10 #tilt
c = 10

start_x = -150
end_x = 150

pen.goto(0,0)
pen.pendown()
pen.goto(0,100)
pen.goto(0,-100)
pen.goto(0,0)
pen.goto(150,0)
pen.goto(-150,0)

pen.penup()
pen.goto(start_x, a * start_x ** 2 + b * start_x + c)
pen.pendown()

for x in range(start_x, end_x +1, 5):
    y = a * x ** 2 + b * c
    pen.goto(x, y)

pen.hideturtle()
screen.mainloop