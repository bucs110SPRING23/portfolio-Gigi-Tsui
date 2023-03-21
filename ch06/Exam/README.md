# CS110 Midterm Exam

## SHORT DESCRIPTION *(1 or 2 sentences describing your program)*

## KNOWN BUGS AND INCOMPLETE PARTS *(list any known bugs or non-working parts)*

## REFERENCES *(any resources you use outside of class materials)*

## MISCELLANEOUS COMMENTS *(anything else you would like the grader to know)*

import turtle

def draw_petal(t, radius, angle):
    """Draw a single petal of the flower"""
    t.circle(radius, angle)
    t.left(180 - angle)
    t.circle(radius, angle)
    t.left(180 - angle)

def draw_flower(t, num_petals, radius, angle):
    """Draw a flower with the given number of petals"""
    for _ in range(num_petals):
        draw_petal(t, radius, angle)
        t.left(360 / num_petals)

def main():
    # Set up the turtle
    t = turtle.Turtle()
    t.speed(0)  # Set the turtle speed to the fastest

    # Draw the flower
    draw_flower(t, 10, 100, 40)

    # Exit on click
    turtle.exitonclick()

if __name__ == '__main__':
    main()
