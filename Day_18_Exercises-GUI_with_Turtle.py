from turtle import Turtle, Screen
import heroes
import random

print(heroes.gen())

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
timmy.speed("fastest")

timmy.forward(100)
timmy.right(90)
for _ in range(4):
    timmy.forward(100)
    timmy.left(90)

timmy.left(180)

for _ in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

timmy.left(90)
timmy.forward(200)

for shape in range(3, 10):
    r = random.random()
    g = random.random()
    b = random.random()
    timmy.pencolor(r, g, b)
    for times in range(shape):
        timmy.forward(100)
        timmy.left(360/shape)

timmy.left(90)
timmy.penup()
timmy.forward(300)
timmy.pendown()

directions = [0, 90, 180, 270]
colors = [0.3, 0.6, 0.9]


def random_color():
    r = random.choice(colors)
    g = random.choice(colors)
    b = random.choice(colors)
    color = (r, g, b)
    return color


timmy.width(5)
for _ in range(30):
    timmy.pencolor(random_color())
    direction = random.choice(directions)
    timmy.setheading(direction)
    timmy.forward(30)

timmy.penup()
timmy.forward(100)
timmy.pendown()
timmy.width(1)
timmy.color("black")
n_circles = 36
for _ in range(n_circles):
    timmy.right(360/n_circles)
    timmy.circle(100)

# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         timmy.color(c)
#         timmy.forward(steps)
#         timmy.right(30)

screen = Screen()
screen.exitonclick()
