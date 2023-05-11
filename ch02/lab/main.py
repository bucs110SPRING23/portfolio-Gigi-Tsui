#Part A
import turtle
window = turtle.Screen()
window.bgcolor("white")

import random 
x = random.randrange (1,10)
print(x)

turt1 = turtle.Turtle()
turt2 = turtle.Turtle()

turt1.color("red")
turt2.color("green")

turt1.up()
turt1.speed(1)
turt2.up()
turt2.speed(1)

#race 1
turt1.forward(random.randrange (1,100))
turt1.goto(-100,20)
turt1.speed(1)
turt2.forward(random.randrange (1,100))
turt2.goto(-100,-20)
turt2.speed(1)

#race 2
for i in range (1,10):
    turt1.forward(random.randrange (1,10))
    turt2.forward(random.randrange (1,10))
turt1.goto(-100,20)
turt2.goto(-100,-20)

window.exitonclick()


#Part B
import pygame
import math
pygame.init()
pygame.event.get
screen = pygame.display.set_mode()

screen.fill("white")
pygame.display.flip()
pygame.time.wait(1000)


shapelist = [3,4,6,20,100,360]
side_length = (50)
xpos=100
ypos=100


for num_sides in shapelist:
    point = []
    for i in range (num_sides):
        angle = 360/num_sides
        radians = math.radians(angle * i)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        point.append ([x,y])
        
    screen.fill("white")
    pygame.draw.polygon(screen, "red", point)
    pygame.display.flip()
    pygame.time.wait(2000)
    

screen.exitonclick()