from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.paddle_up, "Up")
screen.onkeypress(r_paddle.paddle_down, "Down")
screen.onkeypress(l_paddle.paddle_up, "w")
screen.onkeypress(l_paddle.paddle_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_wall()

    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    # detect when right paddle misses the ball
    if ball.xcor() > 400:
        ball.switch_direction()
        scoreboard.left_point()

    # detect when left paddle misses the ball
    if ball.xcor() < -400:
        ball.switch_direction()
        scoreboard.right_point()

screen.exitonclick()
