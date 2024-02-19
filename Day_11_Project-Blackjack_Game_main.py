# Day 11 Project - Blackjack Game

from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def score_calc(cards):
  score = sum(cards)
  loc = -1
  for card in cards:
    if card == 11:
      loc = cards.index(11)
  if score > 21 and loc > -1:
    cards[loc] = 1
    score = sum(cards)
  return score 

def draw_card_player():
  card = random.choice(cards)
  cards_player.append(card)
  score_player = score_calc(cards_player)
  print(f"Your cards: {cards_player}, current score: {score_player}.")
  return score_player

def draw_card_computer():
  card = random.choice(cards)
  cards_computer.append(card)
  score_computer = score_calc(cards_computer)
  print(f"Computer's first card: {cards_computer[0]}.")
  return score_computer

def final_score(cards_p,score_p,cards_c,score_c):
  print(f"Your final hand: {cards_p}, final score: {score_p}.")
  print(f"Computer's final hand: {cards_c}, final score: {score_c}.")

def blackjack():
  
  score_player = draw_card_player()
  
  score_computer = draw_card_computer()
  
  if score_player > 21 or score_computer == 21:
    final_score(cards_player,score_player,cards_computer,score_computer)
    print("You lose.")
    return
  
  draw_cards_answer = input("Type 'y' to get another card, type 'n' to pass: ")
  
  if draw_cards_answer == "y":
    blackjack()
  else:
    while score_computer < 17:
      score_computer = draw_card_computer()
    
    final_score(cards_player,score_player,cards_computer,score_computer)

    if score_player > score_computer:
      print("You win!")
    elif score_player == score_computer and score_player != 21:
      print("It is a draw.")
    elif score_player == score_computer and score_player == 21:
      print("You lose.")
    elif score_player < score_computer and score_computer > 21:
      print("You win!")
    else:
      print("You lose.")

blackjack_round = True
while blackjack_round:
  print(logo)
  blackjack_round_answer = input("Do you want to play Blackjack? Type 'y' or 'n': ")
  if blackjack_round_answer == 'n':
    blackjack_round = False
  else:
    score_player = 0
    score_computer = 0
    cards_player = []
    cards_computer = []
    blackjack()
    
print("Thank you for playing Blackjack!")
