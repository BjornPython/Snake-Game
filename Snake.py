import turtle
from turtle import Screen
from SNAKE_CLASS import Snake

#SNAKE HEAD
snake = Snake()
snake2 = Snake()
snake2.goto(-20, 0)
#SCREEN
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game beta")

turtle.exitonclick()
