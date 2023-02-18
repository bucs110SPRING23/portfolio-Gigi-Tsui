import turtle 

sides= input ("enter the number of sides:")
length = input ("enter the number of sides")

pen = turtle.Turtle()
pen.color("orange")

window = turtle.Screen()

for S in range (sides):
    pen.forward(length)
    pen.right  (360/sides)

window.exitonclick()