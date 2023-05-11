import turtle
import random

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

window = turtle.Screen()
window.bgcolor("pink")

distance = 10
angle = 90
is_in_screen = True

colors = ["red", "green", "blue", "purple", "red"]

while is_in_screen:
    coin = random.randrange (0, 2)
    if coin: #heads
        t.right(angle)
    else: #tails
        t.left(angle)
    t.forward(distance)
    
    turtleX = t.xcor()
    turtleY = t.ycor()
    # x,y = t.pos()

    x_range = window.window_width() / 2
    y_range = window.window_height() / 2

    t.color(random.choice(colors))

    if abs(turtleX) > x_range or abs(turtleY) > y_range:
        is_in_screen = False


window.exitonclick()