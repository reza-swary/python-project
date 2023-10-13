from turtle import Turtle
from random import *
COLORS = ["red", "orange", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_car = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if 1 == randint(1, 6):
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y = randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_car.append(new_car)

    def move_cars(self):
        for car in self.all_car:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += 5
