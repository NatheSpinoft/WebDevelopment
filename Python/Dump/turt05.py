#!/bin/python 
import turtle

#Setup the turtle screen
screen = turtle.Screen()

#create the turtle
pen = turtle.Turtle()
pen.speed(2)

increment = 5
#Draw
for array in range(200):
    pen.down()
    pen.forward(x)
    x += increment

turtle.done()