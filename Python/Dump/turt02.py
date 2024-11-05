import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.setworldcoordinates(-200, -200, 200, 200)

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(1)

# Define the slope (m) and y-intercept (b) for the line y = mx + b
m = 0.5  # slope
b = 10   # y-intercept

# Starting x and ending x values to draw the line
start_x = -150
end_x = 150

# Move to the starting point without drawing
pen.penup()
pen.goto(start_x, m * start_x + b)
pen.pendown()

# Draw the line by calculating points along the line equation
for x in range(start_x, end_x + 1, 10):  # Step by 10 for smoother lines
    y = m * x + b
    pen.goto(x, y)

# Hide the pen after drawing
pen.hideturtle()

# Keep the window open until closed by the user
screen.mainloop()
