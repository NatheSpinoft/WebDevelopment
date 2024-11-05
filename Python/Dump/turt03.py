import turtle

screen = turtle.Screen()
screen.setworldcoordinates(-200, -200, 200, 200)

pen = turtle.Turtle()
pen.speed(3)

m = 0.6
x = 10
b = 10

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
pen.goto(start_x, m * start_x + b)
pen.pendown()

for x in range(start_x, end_x +1, 10):
    y = m * x + b 
    pen.goto(x, y)

pen.hideturtle()
screen.mainloop