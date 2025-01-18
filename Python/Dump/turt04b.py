import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.setworldcoordinates(-200, -200, 200, 200)

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(1)

# Define coefficients for the parabola equation y = ax^2 + bx + c
a = 0.02  # Adjust for the 'width' of the parabola
b = 0     # Adjust for the tilt
c = -50   # Adjust for the vertical position

# Define the range of x-values to draw the parabola
start_x = -150
end_x = 150

# Move to the starting point without drawing
pen.penup()
pen.goto(start_x, a * start_x ** 2 + b * start_x + c)
pen.pendown()

# Draw the parabola by calculating points along the curve
for x in range(start_x, end_x + 1, 5):  # Step by 5 for a smoother curve
    y = a * x ** 2 + b * x + c
    pen.goto(x, y)

# Hide the pen after drawing
pen.hideturtle()

# Keep the window open until closed by the user
screen.mainloop()
