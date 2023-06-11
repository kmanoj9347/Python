# Write a python script using penup and pendown methods to draw “W” character using turtle graphics.
import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Set initial position
start_x = -200
start_y = 0
my_turtle.penup()
my_turtle.setposition(start_x, start_y)
my_turtle.pendown()

# Draw the letter "W"
my_turtle.right(60)
my_turtle.forward(100)
my_turtle.left(120)
my_turtle.forward(100)
my_turtle.right(120)
my_turtle.forward(100)
my_turtle.left(120)
my_turtle.forward(100)

# Exit the turtle graphics window
turtle.done()