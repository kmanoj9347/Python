# Write a python script to draw a triangle using left, right and Forward methods in relative positioning.
import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Draw the triangle
side_length = 200  # Length of each side

my_turtle.forward(side_length)  # Move forward by side_length
my_turtle.left(120)  # Turn left by 120 degrees
my_turtle.forward(side_length)  # Move forward by side_length
my_turtle.left(120)  # Turn left by 120 degrees
my_turtle.forward(side_length)  # Move forward by side_length

# Exit the turtle graphics window
turtle.done()