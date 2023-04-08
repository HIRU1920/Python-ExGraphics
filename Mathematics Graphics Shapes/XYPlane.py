import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the turtle speed and size
t.speed(1)
t.pensize(2)

# Define the colors
colors = ['red', 'green', 'blue', 'purple']

# Draw the X-axis
t.pencolor(colors[0])
t.penup()
t.goto(-300, 0)
t.pendown()
t.goto(300, 0)

# Draw the Y-axis
t.pencolor(colors[1])
t.penup()
t.goto(0, -300)
t.pendown()
t.goto(0, 300)

# Draw the origin point
t.pencolor(colors[2])
t.penup()
t.goto(0, 0)
t.dot(5)

# Add labels to the axes
t.pencolor(colors[3])
t.penup()
t.goto(320, 0)
t.write("X", font=("Arial", 16, "normal"))
t.goto(0, 320)
t.write("Y", font=("Arial", 16, "normal"))

# Hide the turtle
t.hideturtle()

# Keep the window open until closed manually
turtle.done()
