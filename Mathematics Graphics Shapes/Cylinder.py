import turtle

# Set up the turtle
chatgpt_turtle = turtle.Turtle()
chatgpt_turtle.speed(0)
chatgpt_turtle.hideturtle()

# Draw the ChatGPT icon
chatgpt_turtle.color("#FFA500")
chatgpt_turtle.begin_fill()
chatgpt_turtle.circle(100)
chatgpt_turtle.end_fill()
chatgpt_turtle.penup()
chatgpt_turtle.goto(-20, 60)
chatgpt_turtle.pendown()
chatgpt_turtle.color("white")
chatgpt_turtle.begin_fill()
chatgpt_turtle.circle(20)
chatgpt_turtle.end_fill()
chatgpt_turtle.penup()
chatgpt_turtle.goto(-25, 40)
chatgpt_turtle.pendown()
chatgpt_turtle.write("G", font=("Arial", 20, "bold"))

# Exit on click
turtle.exitonclick()
