import turtle

# create a turtle object
t = turtle.Turtle()

# set the number of sides of the decagon
num_sides = 10

# set the length of each side of the decagon
side_length = 100

# set the angle between each side of the decagon
angle = 360 / num_sides

# set the colors to use
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

# move turtle to the starting position
t.penup()
t.goto(0, -50)
t.pendown()

# draw the decagon
for i in range(num_sides):
    # set a color for each side
    color = colors[i % len(colors)]
    t.pencolor(color)
    t.fillcolor(color)
    
    # draw the side
    t.begin_fill()
    t.forward(side_length)
    t.left(angle)
    t.end_fill()

# hide the turtle
t.hideturtle()

# keep the window open until it is closed manually
turtle.done()
