import turtle as t
import random

turtle = t.Turtle()
t.colormode(255)
turtle.shape("arrow")
turtle.speed(0)
turtle.width(1)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + 10)


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()