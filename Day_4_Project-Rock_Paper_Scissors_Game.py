# Day 4 - Rock, Paper, Scissors game

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]
options_name = ["rock", "paper", "scissors"]
print('Welcome to the "Rock, Paper, Scissors" Game!')
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user = int(input())
if user >= 3 or user < 0:
    print("You typed an invalid number, you lose!")
print(options_name[user])
print(options[user])
print("Computer chose:")
computer = random.randint(0, 2)
print(options_name[computer])
print(options[computer])
if user == computer:
    print("It's a draw.")
else:
    if user == 0:
        if computer == 1:
            print("You lose.")
        else:
            print("You win!")
    elif user == 1:
        if computer == 0:
            print("You win!")
        else:
            print("You lose.")
    elif user == 2:
        if computer == 0:
            print("You lose.")
        else:
            print("You win!")
