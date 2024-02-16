# Day 8 Exercises - Functions with Inputs

# Function with no input
def greet():
    print("Hello!")
    print("This is Greet function.")
    print("Thanks!")

greet()

# Function with single input
def greet_with_name(name):
    print(f"Hello, {name}!")
    print("This is Greet function.")
    print("Thanks!")

greet_with_name("Steven")

# Function with multiple inputs
def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"How is it like in {location}?")

# Positional arguments
greet_with("Joe", "Washington DC")

# Keyword arguments
greet_with(location="New York", name="Donald")

# Paint can calculator
import math

def paint_calc(height, width, cover):
    cans = math.ceil(height * width / cover)
    print(f"You'll need {cans} cans of paint.")

test_h = int(input())  # Height of wall (m)
test_w = int(input())  # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# Prime number checker
def prime_checker(number):
    prime = True
    for i in range(2, math.ceil(math.sqrt(number))):
        if number % i == 0:
            prime = False

    if prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input())  # Check this number
prime_checker(number=n)
