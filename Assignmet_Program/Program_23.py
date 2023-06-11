# Write a python script to create your own polygon shape and create an interesting design with it.
import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Set initial position
start_x = 0
start_y = 0
my_turtle.penup()
my_turtle.setposition(start_x, start_y)
my_turtle.pendown()

# Define the number of sides and length of each side of your polygon
num_sides = 8  # Change this to create your desired polygon
side_length = 100  # Change this to adjust the size of your polygon

# Calculate the angle between each side of the polygon
angle = 360 / num_sides

# Draw the polygon
for _ in range(num_sides):
    my_turtle.forward(side_length)
    my_turtle.right(angle)

# Customize the design
my_turtle.color("blue")  # Change the color of the polygon
my_turtle.fillcolor("yellow")  # Change the fill color of the polygon
my_turtle.begin_fill()  # Start filling the polygon

# Draw the filled polygon
for _ in range(num_sides):
    my_turtle.forward(side_length)
    my_turtle.right(angle)

my_turtle.end_fill()  # Finish filling the polygon

# Exit the turtle graphics window
turtle.done()
