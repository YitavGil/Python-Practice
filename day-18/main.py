from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape('turtle')
turtle.color('lime green')


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


dashed_line()





























screen = Screen()
screen.exitonclick()