import turtle
import random

screen = turtle.Screen()
turt1=turtle.RawTurtle(screen)


yes = True
while yes:
    sides = ["head", "tails"]
    flip= random.choice(sides)
    if flip == "heads":
        turt1.left(90)
    else:
        turt1.right(90)
    turt1.forward(50)
    turt1.speed(1)


screen.exitonclick()