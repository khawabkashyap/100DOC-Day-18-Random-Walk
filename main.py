import turtle as t
import random

walk = t.Turtle()

walk.hideturtle()
walk.pensize(15)


def random_color():
    t.colormode(255)
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    walk.color(R, G, B)


def turn():
    return random.choice([0, 90, 180, 270])


while True:
    random_color()
    walk.forward(random.choice([10, 20, 25, 30, 40, 50, 60]))
    walk.speed(-5)

    walk.setheading(turn())
