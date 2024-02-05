# Day 6 Project - Reeborg's World
# You will be able to run this Python code in Reeborg's World environment
# https://reeborg.ca

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()    
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
