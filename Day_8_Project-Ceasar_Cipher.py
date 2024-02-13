# Day 8 Project - Ceasar Cypher 
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def ceasar(start_text, shift_amount, direction_option):
    end_text = ""
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction_option == "encode":
                new_position = (position + shift_amount) % 26
            elif direction_option == "decode":
                new_position = (position - shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {direction_option}d text is {end_text}.")

repeat = "yes"
while repeat == "yes":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceasar(start_text=text, shift_amount=shift, direction_option=direction)

    repeat = input("Do you want to repeat? Type 'Yes' or 'No'.").lower()
   
    if repeat == "no":
      print("Bye!")
