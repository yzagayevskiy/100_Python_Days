from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.1)

    # Detect collision with food
    if snake.head.distance(food) < 1:
        food.refresh()
        scoreboard.increase_score()
        snake.grow()

    # Detect collision with wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for i in snake.t[1:]:
        if snake.head.distance(i) < 1:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
