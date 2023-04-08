import turtle

# create turtle instance
t = turtle.Turtle()

# set speed
t.speed(1)

# set up screen size
turtle.setup(800, 600)

# draw hexagon
t.penup()
t.goto(-50, 0)
t.pendown()
t.color("red", "green")
t.begin_fill()
for i in range(6):
    t.forward(100)
    t.right(60)
t.end_fill()

# keep window open until user closes it
turtle.mainloop()
