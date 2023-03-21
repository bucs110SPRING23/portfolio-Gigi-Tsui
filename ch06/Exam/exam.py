import turtle

def draw_petal(t, radius, angle):
    t.color("cyan")
    t.pensize(3)
    t.circle(radius, angle)
    t.left(180 - angle)
    t.circle(radius, angle)
    t.left(180 - angle)

def draw_flower(t, num_petals, radius, angle):
    for _ in range(num_petals):
        draw_petal(t, radius, angle)
        t.left(360 / num_petals)
        

def draw_stem(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pensize(5)
    t.color("green")
    t.forward(150)

def main():
    t = turtle.Turtle()
    t.speed(100)

    draw_stem(t, 0, 0)
    draw_flower(t, 20, 100, 40)
    turtle.exitonclick()

main()