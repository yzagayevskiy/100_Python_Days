# Day 7 Project - Hangman Game

from replit import clear
import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
print(hangman_art.logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:

    guess = input("Guess a letter: ").lower()
    clear()

    if guess in display:
        print(f"You have already entered letter {guess}.")

    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:  
            display[position] = letter

    if guess not in chosen_word:
        print(f"Entered letter {guess} is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f'The answer is {chosen_word}.')

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
