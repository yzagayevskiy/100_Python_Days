# Day 3 - Conditional Statements if/elif/else

# if/else statements
# Nested if/else statements - Rollercoaster ticket #1
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    age = int(input("What is your age? "))
    if age < 12:
        print("You fare is $5.")
    elif age < 18:
        print("You fare is $7.")
    else:
        print("You fare is $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Multiple if/else statements - Rollercoaster ticket #2
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age < 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Fairy age tickets are free.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken for $3? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your total bill is ${bill}.")

else:
    print("Sorry, you have to grow taller before you can ride.")

# Odd or even number?
number = int(input())
remainder = int(number % 2)
if remainder == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# if/elif/else statements - BMI calculator
# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
BMI = weight / height**2
if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")

# Nested if/else statements - Leap year calculator
# Which year do you want to check?
year = int(input())
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")

# Multiple if statements - Pizza order
print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # What size pizza do you want? S, M, or L
add_pepperoni = input()  # Do you want pepperoni? Y or N
extra_cheese = input()  # Do you want extra cheese? Y or N
bill = 0
if size == 'S':
    bill += 15
    if add_pepperoni == 'Y':
        bill += 2
elif size == 'M':
    bill += 20
    if add_pepperoni == 'Y':
        bill += 3
elif size == 'L':
    bill += 25
    if add_pepperoni == 'Y':
        bill += 3

if extra_cheese == 'Y':
    bill += 1

print(f"Your final bill is: ${bill}.")

# The Love Calculator exercise
print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
name = name1.lower() + name2.lower()
true = name.count("t") + name.count("r") + name.count("u") + name.count("e")
love = name.count("l") + name.count("o") + name.count("v") + name.count("e")
true_love = int(str(true) + str(love))
    print(f"Your score is {true_love}, you go together like coke and mentos.")
  print(f"Your score is {true_love}, you go together like coke and mentos.")
    print(f"Your score is {true_love}, you are alright together.")
  print(f"Your score is {true_love}, you are alright together.")
    print(f"Your score is {true_love}.")
  print(f"Your score is {true_love}.")
