import turtle
from turtle import *
import random
# tim = Turtle()
# tommy = Turtle()
# john = Turtle()
# michael = Turtle()
# taylor = Turtle()
# tim.color = "green"
# tommy.color = "red"
# john.color = "blue"
# michael.color = "yellow"
# taylor.color="black"
all_turtles =[]
screen = Screen()
screen.setup(width=800, height=600)
user_bet = screen.textinput("Make your bet","which turtle will win the race?")
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
y_position = [-70,-40,-10,20,50,80]
for turtle_Index in range (0,len(colors)):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_Index])
    new_turtle.goto(x = -230,y = y_position[turtle_Index])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 300:
            is_race_on = False
            winn_color = turtle.pencolor()
            if winn_color == user_bet:
                print(f"You win! {winn_color} is the winner!")
            else:
                print(f"You lose! {winn_color} is the winner!")
        random_number = random.randint(0,10)
        turtle.forward(random_number)

screen.exitonclick()
