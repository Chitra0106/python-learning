import turtle
timmy = turtle.Turtle()
# for _ in range(100):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
num_sides = 5
angle = 360/num_sides
for _ in range(num_sides):
    timmy.forward(100)
    timmy.left(angle)


