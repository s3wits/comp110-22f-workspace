"""Chardle excersice"""
__author__ = "730555430"

input_word: str = input("Name a 5 letter word: ")
if len(input_word) != 5:
    print("Word must be 5 characters long!")
    quit()
guess_letter: str = input("Name a letter: ")
if len(guess_letter) != 1:
    print("Please input 1 character!")
    quit()
print("Searching for " + guess_letter + " in " + input_word)

x: int = (0)
if guess_letter == input_word[0]:
    print(guess_letter + " found at index 0")
    x = x + 1
if guess_letter == input_word[1]:
    print(guess_letter + " found at index 1")
    x = x + 1
if guess_letter == input_word[2]:
    print(guess_letter + " found at index 2")
    x = x + 1
if guess_letter == input_word[3]:
    print(guess_letter + " found at index 3")
    x = x + 1
if guess_letter == input_word[4]:
    print(guess_letter + " found at index 4")
    x = x + 1
print( str(x) + " instances of " + guess_letter + " found in " + input_word)