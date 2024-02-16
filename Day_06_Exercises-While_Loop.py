# Day 6 Exercises - While Loop
# You will be able to run this Python code in Reeborg's World environment
# https://reeborg.ca

def turn_around():
    turn_left()
    turn_left()
    
def move_steps(steps):
    for i in range(0,steps):
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
# Return in a straight line move
move_steps(2)
turn_around()
move_steps(2)
turn_around()

# Square move
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()
turn_around()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    move()
    jump()
   
number_of_jumps = 6
while number_of_jumps > 0:
    move()
    jump()
    number_of_jumps -= 1

while not at_goal():
    move()
    jump()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
        
def jump_high():
    turn_left()
    move()
    count = 1
    while wall_on_right():
        move()
        count += 1
    else:
        turn_right()
        move()
        turn_right()
        for i in range(count):
            move()
    turn_left()
        
while not at_goal():
    if wall_in_front():
        jump_high()
    else:
        move()
