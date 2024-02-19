# Day 12 Project - Number Guessing Game

# Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

logo = """  ___    __    __  __  ____ 
 / __)  /__\  (  \/  )( ___)
( (_-. /(__)\  )    (  )__) 
 \___/(__)(__)(_/\/\_)(____)"""

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)

level = input("Chose a difficulty. Type 'easy' or 'hard': ")

if level == "easy":
  attempt = 10
elif level == "hard":
  attempt = 5
  
print("You have " + str(attempt) + " attempts remaining to guess the number.")

while attempt > 0:
  guess = int(input("Make a guess: "))
  if guess == number:
    print("You got it! The answer was " + str(number))
    print("You win!")
    attempt = 0
  elif guess > number:
    print("Too high.")
    print("Guess again.")
    attempt -= 1
    if attempt == 0:
      print("You've run out of guesses, you lose.")
    else:
      print("You have " + str(attempt) + " attempts remaining to guess the number.")
  elif guess < number:
    print("Too low.")
    print("Guess again.")
    attempt -= 1
    if attempt == 0:
      print("You've run out of guesses, you lose.")
    else:
      print("You have " + str(attempt) + " attempts remaining to guess the number.")
