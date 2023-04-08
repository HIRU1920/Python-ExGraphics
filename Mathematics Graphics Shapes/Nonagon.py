import turtle

# create turtle instance
t = turtle.Turtle()

# set speed
t.speed(1)

# set up screen size
turtle.setup(800, 600)

# draw nonagon
t.penup()
t.goto(-50, 0)
t.pendown()
t.color("green", "red")
t.begin_fill()
for i in range(9):
    t.forward(120)
    t.right(360/9)
t.end_fill()

# keep window open until user closes it
turtle.mainloop()
