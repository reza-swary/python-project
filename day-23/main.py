import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
screen.listen()
scoreboard = Scoreboard()
screen.onkey(player.move, "Up")
screen.onkey(player.move_back, "Down")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    for i in car_manager.all_car:
        if i.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() > 280:
        player.goto_start()
        car_manager.level_up()
        scoreboard.level_up()
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
screen.exitonclick()
