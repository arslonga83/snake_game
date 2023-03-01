from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.colormode(255)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
current_color = "blue"


# added feature to randomize food color and add that same color segment to the snake
def get_next_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        snake.extend(current_color)
        current_color = get_next_color()
        food.refresh(current_color)
        scoreboard.score_point()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
