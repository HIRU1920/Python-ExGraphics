import turtle
import math

# Create a turtle object
t = turtle.Turtle()

# Set the turtle speed and size
t.speed(0)
t.pensize(2)

# Set the length and frequency of the wave
length = 300
frequency = 3

# Move the turtle to the starting position
t.penup()
t.goto(-length/2, 0)
t.pendown()

# Draw the cosine wave
for x in range(-int(length/2), int(length/2)):
    y = 50 * math.cos(x * math.pi / 180 * frequency)
    t.goto(x, y)

# Hide the turtle
t.hideturtle()

# Keep the window open until closed manually
turtle.done()
