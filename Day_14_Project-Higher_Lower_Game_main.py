from replit import clear
from art import logo
from art import vs
from game_data import data
import random
# Data is a list of dictionaries
# Each dictionary has the following keys:
# 0 - "name"
# 1 - "follower_count"
# 2 - "description"
# 3 - "country"

data_entries = len(data)

def compare(index1,index2,user):
  answer = False
  if data[index1]["follower_count"] > data[index2]["follower_count"] and user == "A":
    answer = True
  if data[index1]["follower_count"] < data[index2]["follower_count"] and user == "B":
    answer = True
  return answer

def higher_lower():
  print(logo)
  correct = True
  score = 0
  contestant1 = random.randint(0,data_entries-1)
  while correct:
    print(f"Compare A: {data[contestant1]['name']}, {data[contestant1]['description']},\
 from {data[contestant1]['country']}.")
    print(vs)
    contestant2 = random.randint(0,data_entries-1)
    print(f"Against B: {data[contestant2]['name']}, {data[contestant2]['description']},\
 from {data[contestant2]['country']}.")
    guess = input("Who has more followers? Type 'A' or 'B': ")
    correct = compare(contestant1,contestant2,guess)
    if correct:
      score += 1
      clear()
      print(logo)
      print(f"You're right! Current score: {score}.")
      contestant1 = contestant2
    else:
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}.")

higher_lower()
