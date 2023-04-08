import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the color of the turtle's pen
t.color("red", "green")

# Draw the right angle triangle
t.forward(200)  # Draw the base of the triangle
t.left(90)     # Turn left
t.forward(200)  # Draw the vertical side of the triangle
t.left(135)     # Turn left at 135 degrees
t.color("blue", "yellow")
t.forward(284)  # Draw the diagonal side of the triangle

# Write the angle names
t.penup()
t.goto(75, -10)
t.write("90", font=("Arial", 16, "normal"))
t.goto(10, 125)
t.write("45", font=("Arial", 16, "normal"))
t.goto(190, 125)
t.write("45", font=("Arial", 16, "normal"))

# Write the point names
t.goto(-15, -15)
t.write("A", font=("Arial", 16, "normal"))
t.goto(215, -15)
t.write("B", font=("Arial", 16, "normal"))
t.goto(90, 150)
t.write("C", font=("Arial", 16, "normal"))

# Hide the turtle
t.hideturtle()

# Exit on click
turtle.exitonclick()

