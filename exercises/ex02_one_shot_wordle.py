"""Ex02 - One Shot Wordle."""

__author__ = "730555430"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

correct_guess: str = "adirae"

guess: str = input(f"What is your {str(len(correct_guess))}-letter guess? ")
while len(guess) != len(correct_guess):
    if len(guess) != len(correct_guess):
        print(f"That was not {str(len(correct_guess))} letters! Try again: ")
        guess = input("")

index_counter: int = 0
emoji_string: str = ""

while (index_counter < len(correct_guess)):
    if guess[index_counter] == correct_guess[index_counter]:
        emoji_string += GREEN_BOX
    else: 
        yellow_counter: int = 0
        yellow_checker: bool = False
        while yellow_counter < len(guess):
            if guess[index_counter] == correct_guess[yellow_counter]:
                yellow_checker = True
            yellow_counter += 1
        if yellow_checker:
            emoji_string += YELLOW_BOX
        else:
            emoji_string += WHITE_BOX
    index_counter += 1

print(emoji_string)

if len(guess) == len(correct_guess):
    if guess != correct_guess:
        print("Not quite. Play again soon!")
    else:
        print("Woo! You got it!")
