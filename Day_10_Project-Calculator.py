# Day 10 - Project - Calculator

from art import logo
from replit import clear

def add(a,b):
  return a + b
def sub(a,b):
  return a - b
def mul(a,b):
  return a * b
def div(a,b):
  return a / b

operations = {
  "+": add,
  "-": sub,
  "*": mul,
  "/": div,
}

choice2 = True
while choice2:
  clear()
  print(logo)
  
  number1 = float(input("What's the first number?: "))

  for symbol in operations:
    print(symbol)
  
  choice = "y"
  while choice == 'y':
    operation = input("Pick an operation: ")
    number2 = float(input("What's the next number?: "))
    number3 = operations[operation](number1,number2)
    print(f"{number1} {operation} {number2} = {number3}")
    
    choice = input(
        f"Type 'y' to continue calculating with {number3}, or type 'n' to start a new operation, or type 'e' to exit the calculator: "
    )

    number1 = number3
    
    if choice == 'e':
      choice2 = False    
