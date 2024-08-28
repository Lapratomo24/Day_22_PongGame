import turtle
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.goto(x=350, y=0)
paddle.color("white")
paddle.penup()


def paddle_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def paddle_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(paddle_up, "Up")
screen.onkey(paddle_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()
