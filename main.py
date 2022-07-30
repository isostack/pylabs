# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

from ast import excepthandler
from xml.etree.ElementTree import TreeBuilder
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def check_board():
    word = input("Enter a word: ").upper()
    try:  
        output_list = [phonetic_dict[letter] for letter in word] 
    except KeyError: 
        print("Invalid input or text")
        check_board()
    else:  
        print(output_list)

check_board()