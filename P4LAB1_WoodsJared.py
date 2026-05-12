# Jared Woods
# 5 April 2026
# Assignment Name: Turtle House Drawing
# This program uses turtle graphics to draw a house
# made of a square and triangle using both for and while loops.

import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create turtle
house = turtle.Turtle()
house.color("darkgreen")
house.pensize(3)
house.speed(3)

# Move turtle to starting position
house.penup()
house.goto(-70, -100)
house.pendown()

# Draw square using FOR loop
for i in range(4):
    house.forward(140)
    house.left(90)

# Move to top of square for roof
house.penup()
house.goto(-70, 40)
house.pendown()

# Set roof fill color to brown
house.fillcolor("brown")

# Start filling the triangle
house.begin_fill()

# Draw triangle using WHILE loop
count = 0
while count < 3:
    house.forward(140)
    house.left(120)
    count += 1

# Finish filling the roof
house.end_fill()

# Keep window open
turtle.done()