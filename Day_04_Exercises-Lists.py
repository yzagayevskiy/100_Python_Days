# Day 4 Exercises - Lists

import random
import my_module
import string

# Pseudo-random number generation
random_integer = random.randint(1, 10)
random_float = random.random()
print(random_integer)
print(random_float)

# My module
print(my_module.pi)

# Heads - tails coin toss
random_number = random.randint(0, 1)
if random_number == 0:
    print("Tails")
else:
    print("Heads")

# List of the US states in order of joining the union
list_of_states = [
    "delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
    "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
    "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
    "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
    "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
    "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
    "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"
]

print(list_of_states[0])
print(list_of_states[-1])

list_of_states[0] = "Delaware"
print(list_of_states[0])

list_of_states.append("Puerto Rico")
print(list_of_states)

# Random number generator to choose a person who buys a meal today
names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
number = len(names)
random_name = names[random.randint(0, number - 1)]
print(f"{random_name} is going to buy the meal today!")

# Nested list
fruits = [
    "Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries",
    "Pears"
]
vegetaables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetaables]
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[0][0])

# Treasure map exercise
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure? e.g. B1
position_list = list(position)
alphabet = string.ascii_uppercase
i = int(alphabet.index(position_list[0]))
j = int(position_list[1])
map[j-1][i] = "X"
print(f"{line1}\n{line2}\n{line3}")
