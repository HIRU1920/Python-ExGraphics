import turtle

# create turtle instance
t = turtle.Turtle()

# set speed
t.speed(1)

# set up screen size
turtle.setup(800, 600)

# draw heptagon
t.penup()
t.goto(-70, 0)
t.pendown()
t.color("blue", "black")
t.begin_fill()
for i in range(7):
    t.forward(140)
    t.right(360/7)
t.end_fill()

# keep window open until user closes it
turtle.mainloop()
