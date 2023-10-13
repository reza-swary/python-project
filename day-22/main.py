from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from time import sleep
from score1 import Score


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)
l_paddle = Paddle((-380, 0))
r_paddle = Paddle((375, 0))
ball = Ball()
score1 = Score((-100, 200))
score2 = Score((100, 200))
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_Down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_Down, "s")
game_is_on = True
sp2 = float(ball.speed1())
while game_is_on:
    screen.update()
    ball.move()

    sleep(sp2)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce(1)
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.bounce(2)

    elif ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce(2)

    if ball.xcor() > 380:
        score1.add_score()
        ball.reset_position()
        sleep(2)
    elif ball.xcor() < -380:
        score2.add_score()
        ball.reset_position()
        sleep(2)
screen.exitonclick()
