import time
import turtle
from turtle import Screen
from SNAKE_CLASS import Snake
from snake_food import Food
from snake_scoreboard import ScoreBoard

# SNAKE BODY, FOOD, SCOREBOARD
snake = Snake()
food = Food()
score = ScoreBoard()

# SCREEN
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game beta")
screen.tracer(0)  # IMPORTANT
screen.listen()  # IMPORTANT
screen.onkey(snake.move_up, "w")
screen.onkey(snake.move_down, "s")
screen.onkey(snake.move_left, "a")
screen.onkey(snake.move_right, "d")

# WHILE LOOP FOR THE GAME
game = True
while game:
    screen.update()  # Updates the screen
    time.sleep(0.1)  # How fast the screen updates
    if snake.head.distance(food) < 15:  # if Snake eats a food...
        food.spawn()  # Spawns food
        snake.add_body()  # Adds a new body
        score.add_score()  # Adds 1 to the score

    snake.update_position()  # Updates the position of the snake's body

    if snake.collision():  # If snake collides with wall or tail...
        score.game_over()  # Shows "GAME OVER" On screen
        game = False
    snake.move()  # Moves the snake's body and its head

turtle.exitonclick()
