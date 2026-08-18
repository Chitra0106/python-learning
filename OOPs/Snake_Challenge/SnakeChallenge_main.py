from turtle import Turtle, Screen
import time
from Snake import Snake
from Food import Food

screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.left, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)
    snake.move()
    #Detect the food
    if snake.head.distance(food) < 15:
        food.refresh()


screen.exitonclick()

