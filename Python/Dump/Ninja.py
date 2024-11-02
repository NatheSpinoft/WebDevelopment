import turtle

# Create a Turtle object
ninja = turtle.Turtle()

# Set the speed of the turtle (optional, higher value is faster)
ninja.speed(20)

# Loop to create the design
for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)

    ninja.penup()
    ninja.setposition(0, 0)  # Return to the center
    ninja.pendown()
    
    ninja.right(2)  # Rotate slightly for the next iteration

# Keep the window open until the user closes it
turtle.done()
