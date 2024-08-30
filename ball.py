from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")

    def move(self):
        new_x = self.xcor() + 20
        new_y = self.ycor() + 20
        self.goto(new_x, new_y)