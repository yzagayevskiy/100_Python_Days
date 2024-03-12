import colorgram
from turtle import Turtle, Screen
import random


n_colors = 24
colors = colorgram.extract('painting.jpg', n_colors)

colors_list = []
colors_tuple = []
for item in range(n_colors):
    color = colors[item]
    colors_list.append(color.rgb)
    colors_tuple.append((colors_list[item][0], colors_list[item][1], colors_list[item][2]))

print(colors_tuple)

colors_tuple_cleaned = [(252, 244, 249), (214, 152, 103), (14, 19, 65), (46, 93, 150), (239, 227, 93), (122, 171, 208),
                        (206, 80, 114), (172, 83, 38), (139, 23, 48), (13, 42, 23), (199, 135, 165), (47, 26, 16),
                        (28, 44, 133), (111, 196, 161), (156, 61, 89), (37, 128, 65), (225, 77, 52), (80, 18, 40),
                        (147, 216, 180), (10, 98, 32), (98, 112, 188)]

tim = Turtle()
tim.speed("fastest")
tim.hideturtle()
screen = Screen()
screen.colormode(255)

nx = 10
ny = 10
dx = 50
dy = 50
size = 20
x_start = - nx * dx / 2
y_start = - ny * dy / 2
tim.penup()
for iy in range(ny):
    for ix in range(nx):
        x = x_start + ix * dx + dx / 2
        y = y_start + iy * dy + dy / 2
        tim.setx(x)
        tim.sety(y)
        tim.dot(size, random.choice(colors_tuple_cleaned))

screen.exitonclick()
