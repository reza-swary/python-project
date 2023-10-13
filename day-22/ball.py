from turtle import Turtle
from random import *


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("slowest")
        self.y_move = randint(-10, 10)
        self.x_move = randint(-10, 10)
        self.speed1 = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, x):
        if x == 1:
            self.y_move *= -1
        elif x == 2:
            self.x_move *= -1
            self.speed1 *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.speed1 = 0.1
        self.bounce(2)
