
"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word_format = input("Enter the format of a word: ")
word = ""
for kind in word_format:
    if kind == "#":
        word += random.choice(CONSONANTS)
    elif kind == "%":
        word += random.choice(VOWELS)
    elif kind == "*":
        word += random.choice(VOWELS + CONSONANTS)
    elif kind.lower() in VOWELS or CONSONANTS:
        word += kind

print(word)
