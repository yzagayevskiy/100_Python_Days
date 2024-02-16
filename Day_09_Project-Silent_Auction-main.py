# Day 9 Project - Silent Auction

from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")

bidders = {}
more_bidders = True
while more_bidders:
  name = input("What is your name?: ")
  bid = input("What is your bid?: $")
  bidders[name] = bid
  answer = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
  if answer == "no":
    more_bidders = False
  clear()

winner = max(bidders, key=bidders.get)
winning_bid = bidders[winner]

print("The winner is " + winner + " with a bid of $" + winning_bid)
