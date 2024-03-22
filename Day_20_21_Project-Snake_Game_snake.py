from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.nt = 3
        self.t = []
        self.create_snake()
        self.head = self.t[0]

    def create_snake(self):
        for i in range(self.nt):
            self.t.append(Turtle())
            self.t[i].color("white")
            self.t[i].shape("square")
            self.t[i].penup()
            x = - i * 20
            y = 0
            self.t[i].setposition(x, y)

    def move(self):
        for i in range(len(self.t) - 1, 0, -1):
            x_new = self.t[i - 1].xcor()
            y_new = self.t[i - 1].ycor()
            self.t[i].setposition(x_new, y_new)
        self.head.forward(MOVE_DISTANCE)

    def grow(self):
        self.t.append(Turtle())
        self.t[self.nt].color("white")
        self.t[self.nt].shape("square")
        self.t[self.nt].penup()
        x = self.t[self.nt - 1].xcor()
        y = self.t[self.nt - 1].ycor()
        self.t[self.nt].setposition(x, y)
        self.nt += 1

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.t[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.t[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.t[0].setheading(RIGHT)
