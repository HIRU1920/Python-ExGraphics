import turtle

# create turtle instance
t = turtle.Turtle()

# set speed
t.speed(1)

# set up screen size
turtle.setup(800, 600)

# draw pentagon
t.penup()
t.goto(-100, 0)
t.pendown()
t.color("red", "yellow")
t.begin_fill()
for i in range(5):
    t.forward(200)
    t.right(72)
t.end_fill()

# keep window open until user closes it
turtle.mainloop()
