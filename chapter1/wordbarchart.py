import sys
import pprint
import unidecode 
from collections import defaultdict

def main():
    """returns the number of each alphabets appear"""  

    text = input("Input sentence you like\n")
    text = unidecode.unidecode(text)
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

    mapped = defaultdict(list)
    for character in text:
        character = character.lower()
        if character in ALPHABET:
            mapped[character].append(character)
        
    pprint.pprint(mapped)

if __name__ == "__main__":
    main()