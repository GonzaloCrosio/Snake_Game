from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen creation and configuration
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# Nothing happens until the update occurs
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# o listen to the events 
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    # To update the screen only once all the 'for in' loop has been executed
    screen.update()
    time.sleep(0.1)                         # Snake speed
    snake.move()

    # To detect collision between the snake and the food
    if snake.head.distance(food) < 15:      # If the distance is less than 15, it detects the collision between the snake and the food
        food.refresh()                      # Create a new food
        snake.extend()                      # Add segment to snake
        scoreboard.increase_score()         # Call function score +1

    # o detect collision between the snake and the wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset()

    # To detect the collision of the snake with itself
    for segment in snake.segments:          # To analyze the segments of the snake that approach within a distance of 10.
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
