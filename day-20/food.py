from turtle import Turtle
from random import *
num1 = []
for i in range(-280, 280, 20):
    num1.append(i)


class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = choice(num1)
        random_y = choice(num1)
        self.goto(random_x, random_y)
