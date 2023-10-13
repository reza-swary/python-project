from turtle import Screen, Turtle
from time import sleep
from snake import Snake
from food import Food
from score import Score

screen = Screen()
snake = Snake()
food = Food()
score = Score()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake")
screen.tracer(0)
keep_moving = True
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

all_turtle = []


while keep_moving:
    screen.update()
    sleep(0.1)
    snake.move()
    if snake.seg[0].distance(food) < 5:
        food.refresh()
        snake.extend()
        score.add_score()
    if snake.seg[0].xcor() > 280 or snake.seg[0].xcor() < -285 or snake.seg[0].ycor() < -285 or snake.seg[0].ycor() > 300:
        score.reset()
        snake.reset()

    for segment in snake.seg:
        if segment == snake.seg[0]:
            pass
        elif snake.seg[0].distance(segment) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()
