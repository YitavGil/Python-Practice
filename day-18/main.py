from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape('turtle')
turtle.color('lime green')
turtle.pensize(5)


# Make square
def make_square():
    for _ in range(4):
        turtle.forward(150)
        turtle.right(90)


def dashed_line():
    for _ in range(5):
        turtle.forward(20)
        turtle.penup()
        turtle.forward(20)
        turtle.pendown()


def create_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)


def random_walk():
    colors = ['red', 'blue', 'green', 'yellow', 'purple']
    directions = [0, 90, 180]
    for _ in range(200):
        turtle.color(random.choice(colors))
        turtle.forward(30)
        turtle.setheading(random.choice(directions))





























screen = Screen()
screen.exitonclick()