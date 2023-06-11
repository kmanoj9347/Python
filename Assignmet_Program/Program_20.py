import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Set the initial position of the turtle
x = -100  # X-coordinate
y = -100  # Y-coordinate
my_turtle.penup()
my_turtle.setposition(x, y)
my_turtle.pendown()

# Draw the square
side_length = 200  # Length of each side
for _ in range(4):
    my_turtle.forward(side_length)
    my_turtle.right(90)

# Exit the turtle graphics window
turtle.done()