import turtle
import random

# Create a turtle object
t = turtle.Turtle()

# Set the turtle speed and size
t.speed(1)
t.pensize(3)

# Draw the circle
t.penup()
t.goto(0, -100)
t.pendown()
t.color('black', 'white')
t.begin_fill()
t.circle(100)
t.end_fill()

# Draw the triangle
t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(60)
t.color('red')
t.begin_fill()
t.forward(100)
t.setheading(-60)
t.color('green')
t.forward(100)
t.setheading(180)
t.color('blue')
t.forward(100)
t.end_fill()

# Hide the turtle
t.hideturtle()

# Keep the window open until closed manually
turtle.done()
