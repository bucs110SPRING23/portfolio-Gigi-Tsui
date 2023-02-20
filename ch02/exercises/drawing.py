import turtle 



sides = int(input ("enter the number of sides:"))
length = int(input ("enter the length of sides:"))

my_turtle = turtle.Turtle()
my_turtle.color("orange")


window = turtle.Screen()

for S in range (sides):
    my_turtle.forward(length)
    my_turtle.right  (360/sides)

sides = 6
print((sides-2)*180/sides)

window.exitonclick()




