from turtle import Turtle, Screen, colormode, pensize
import random as rn
timmy = Turtle()


colormode(255)
timmy.pensize(1)
timmy.speed("fastest")


def color():
    r = rn.randint(30, 255)
    g = rn.randint(30, 255)
    b = rn.randint(30, 255)
    color = (r, g, b)
    return color


for _ in range(1000):
    curr_heading = timmy.heading()
    timmy.color(color())
    timmy.circle(100)
    timmy.setheading(curr_heading + 10)


screen = Screen()
screen.exitonclick()
