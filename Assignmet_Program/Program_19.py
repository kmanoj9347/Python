import turtle
my_turtle = turtle.Turtle()
my_turtle.shape('polygon')
n = 6  # Number of sides
side_length = 100  # Length of each side
my_turtle.shapesize(outline=n, stretch_len=side_length/20)
my_turtle.color('blue')
my_turtle.fillcolor('yellow')
my_turtle.penup()
my_turtle.goto(-200, 0)
my_turtle.pendown()
for _ in range(n):
    my_turtle.stamp()
    my_turtle.forward(side_length)
    my_turtle.right(360 / n)
    my_turtle.hideturtle()
turtle.done()