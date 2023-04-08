import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
t = turtle.Turtle()

# Move the turtle to the origin
t.penup()
t.goto(0, 0)
t.pendown()

# Draw the X and Y axes
t.pensize(2)
t.color("black")
t.forward(200)
t.penup()
t.goto(0, 0)
t.pendown()
t.left(90)
t.forward(200)

# Label the axes
t.penup()
t.goto(220, 0)
t.write("X", font=("Arial", 16, "normal"))
t.goto(0, 220)
t.write("Y", font=("Arial", 16, "normal"))

# Draw the grid lines
t.pensize(1)
t.color("lightgray")
for i in range(-200, 201, 20):
    t.penup()
    t.goto(i, -200)
    t.pendown()
    t.goto(i, 200)
    t.penup()
    t.goto(-200, i)
    t.pendown()
    t.goto(200, i)

# Draw some colorful points
t.pensize(5)
t.color("red")
t.dot(10)
t.color("green")
t.goto(50, 50)
t.dot(10)
t.color("blue")
t.goto(-100, 100)
t.dot(10)

# Hide the turtle
t.hideturtle()

# Keep the turtle window open until it is closed
turtle.done()