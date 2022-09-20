from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.spawn()

    def spawn(self):
        """Spawns food randomly"""
        new_x = randint(-280, 280)
        new_y = randint(-280, 280)
        self.goto(new_x, new_y)
