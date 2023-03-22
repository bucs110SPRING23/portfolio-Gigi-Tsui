import turtle

def draw_petals(t, radius, angle):
    t.color("cyan")
    t.pensize(3)
    t.circle(radius, angle)
    t.left(180 - angle)
    t.circle(radius, angle)
    t.left(180 - angle)

def draw_flowers(t, petals, radius, angle):
    for _ in range(petals):
        draw_petals(t, radius, angle)
        t.left(360 /petals)
        

def draw_stem(t, x, y): 
    t.penup()
    t.goto(-100, y)
    t.pendown()
    t.pensize(5)
    t.color("green")
    t.forward(150)

def main():
    t = turtle.Turtle() 
    t.speed(100)

    draw_stem(t, 0, 0)
    draw_flowers(t, 20, 100, 40)
    turtle.exitonclick()

main() 