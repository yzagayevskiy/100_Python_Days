# Day 2 Project - Tip Calculator
# Notes:
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")

bill = input("What was the total bill? $")
tip_percent = input("How much tip would you like to give in %? for example, 15, 18, or 20? ")
num_people = input("How many people to split the bill? ")
pay_share = float(bill) * (1 + float(tip_percent) / 100) / float(num_people)

print(f"Each person should pay: ${pay_share:.2f}")
