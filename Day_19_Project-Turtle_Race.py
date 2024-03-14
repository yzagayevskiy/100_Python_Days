from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "green", "blue", "black"]

n_turtles = 4
turtles = []
for turtle in range(n_turtles):
    turtles.append(Turtle(shape="turtle"))
    turtles[turtle].color(colors[turtle])
    turtles[turtle].penup()
    turtles[turtle].setposition(-240, -100 + 200 * turtle/n_turtles)

user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win a race? Red, green, blue, or black?")
user_bet = user_bet.lower()

race_is_on = True
winning_turtle = "blank"
while race_is_on:
    i_turtle = 0
    for turtle in turtles:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        if turtle.xcor() > 240:
            race_is_on = False
            winning_turtle = turtle.color()[0]

if user_bet == winning_turtle:
    print(f"The winning turtle color is {winning_turtle}. You win!")
else:
    print(f"The winning turtle color is {winning_turtle}. You loose!")

screen.exitonclick()
