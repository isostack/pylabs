#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = []


for item in range(0 , nr_letters):
    password.append(random.choice(letters))
for item in range(0 , nr_symbols):
    password.append(random.choice(symbols))
for item in range(0 , nr_numbers):
    password.append(random.choice(numbers))
print(password)
pass_size =  nr_letters + nr_numbers + nr_symbols

randomer = []

for item in range(0 , pass_size):
    random.shuffle(randomer)
    randomer.append(item)

password = [password[i] for i in randomer]
result = ''.join([str(elem) for elem in password])
print(result)
#Hard Leve - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

print(logo)
game_is_done = False
lives = len(stages - 1)

chosen_word = random.choice(word_list)

print(f"Chosen word is {chosen_word}")

display = []

for item in chosen_word:
    display.append("_")

while not game_is_done:
    guess = input("\nGuess a word!!!: ").lower()
    
    #use the clear function to clear the console -- imported from replit
    clear()

    if guess in display:
        print(f"Youve already guessed {guess}")
    
    for position in range(len(chosen_word)):
        item = chosen_word[position]
        if item == guess:
            display[position] = item
    print(f"{' '.join(display)}")

    if not "_" in display:
        game_is_done = True
        print("You Win!!")

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_is_done = True
            print("You lose!!")   

    print(stages[lives])
    import math
import time

print("Caeser Cipher\n")

def interface():
    switch = input("Function type? Type 'encrypt' | 'decrypt': ")

    if switch == 'encrypt':
        print("\nStarting Encryption...")
        time.sleep(1)
    else:
        print("\nStarting Decryption...")
        time.sleep(1)

    text = input("\nType your message:\n").lower()

    shift = int(input("\nType your shift number:\n")) % 26

    main(text, shift, switch)


drum = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]


def main(x, y, z):
    result = ''
    if z == 'decrypt':
        y *= -1
    for item in x:
        if item in drum:
            result += drum[drum.index(item) + y]
        else:
            result += item
    print(f"The {z}ed text is {result}")
    rerun = input("Do you want to run again? Yes / No :")
    if rerun == "Yes":
        interface()
    else:
        print('Goodbye!!!')

interface()
