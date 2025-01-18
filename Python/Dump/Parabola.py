import turtle

# Create a screen and set its size
screen = turtle.Screen()
screen.setworldcoordinates(-100, -100, 100, 100)  # Adjust the size to fit the parabola

# Create a turtle object
pen = turtle.Turtle()

# Define the parabola equation y = ax^2 (simplified version)
a = 0.01  # Coefficient to control the "width" of the parabola

# Lift the pen to start at the first point without drawing
pen.penup()

# Start drawing the parabola
for x in range(-100, 101):  # Loop through x values (from -100 to 100)
    y = a * x**2  # Calculate y based on the equation y = ax^2
    pen.goto(x, y)  # Move the turtle to the new point (x, y)
    pen.pendown()  # Start drawing after the first point

# Keep the window open until closed by the user
turtle.done()
