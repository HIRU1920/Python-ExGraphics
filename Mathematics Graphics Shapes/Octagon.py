import turtle

# create turtle instance
t = turtle.Turtle()

# set speed
t.speed(1)

# set up screen size
turtle.setup(800, 600)

# draw octagon
t.penup()
t.goto(-50, 0)
t.pendown()
t.color("purple", "orange")
t.begin_fill()
for i in range(8):
    t.forward(100)
    t.right(45)
t.end_fill()

# keep window open until user closes it
turtle.mainloop()
