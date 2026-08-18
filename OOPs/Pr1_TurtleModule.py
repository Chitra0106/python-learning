from turtle import Screen

import Pr1_ImportModule

print(Pr1_ImportModule.anothermodule())

import turtle
timmy = turtle.Turtle()
timmy.color("Black","Brown")
timmy.shape("turtle")
#timmy.speed(0)
timmy.forward(100)
print(timmy)
print(Screen().canvwidth)
Screen().exitonclick()