"""EX01 - Chardle - A cute step towards Wordle."""

__author__ = "730555430"

input_word: str = input("Enter a 5-character word: ")
if len(input_word) != 5:
    print("Error: Word must contain 5 characters")
    quit()
guess_letter: str = input("Enter a single character: ")
if len(guess_letter) != 1:
    print("Error: Character must be a single character.")
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
if x >= 2:
    print(str(x) + " instances of " + guess_letter + " found in " + input_word)
if x == 1:
    print(str(x) + " instance of " + guess_letter + " found in " + input_word)
if x == 0:
    print("No instances of " + guess_letter + " found in " + input_word)
