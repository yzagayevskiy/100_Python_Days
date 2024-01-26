# Day 2 - Data Types, Data Types Conversions and f-String

# Data Types
# String
print("Hello"[0])
print("123" + "345")
# Integer
print(123 + 345)
# Floating point number = Float
print(3.14159)
# Boolean
print(True)
print(False)

# Data type conversion/casting
len_name = len(input("What is your name?"))
print(type(len_name))
print("Your name has " + str(len_name) + " characters.")

# Example, the code adds the two digits of a two digit number
two_digit_number = input()
print(int(two_digit_number[0]) + int(two_digit_number[1]))

# Example, BMI calculator
height = input()
weight = input()
BMI = float(weight) / float(height)**2
print(int(BMI))

# f-String
score = 5
height = 1.8
isWinning = True
print(
    f"Your score is {score}, your height is {height}, you are winning is {isWinning}."
)

# Example, how many weeks left in your life before you turn 90
age = input()
age_as_float = float(age)
weeks_as_int = int((90.0 - age_as_float) * 52)
print(f"You have {weeks_as_int} weeks left.")
