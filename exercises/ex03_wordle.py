"""Wordle - final."""

__author__ = "730555430"


def contains_char(correct_word: str, letter: str) -> bool:
    """To see if a letter is in a word."""
    assert len(letter) == 1
   
    contains_char: bool = False
    index_counter: int = 0

    while (index_counter < len(correct_word)):
        if correct_word[index_counter] == letter:
            contains_char = True
        index_counter += 1
    return contains_char


def emojified(guess: str, correct_word: str) -> str:
    """Emojifies a guess."""
    assert len(guess) == len(correct_word)
    
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    emoji_string: str = ""
    index_counter: int = 0

    while (index_counter < len(correct_word)):
        if guess[index_counter] == correct_word[index_counter]:
            emoji_string += GREEN_BOX
        else: 
            if contains_char(correct_word, guess[index_counter]):
                emoji_string += YELLOW_BOX
            else:
                emoji_string += WHITE_BOX
        index_counter += 1
    return emoji_string
   

def input_guess(length: int) -> str:
    """Makes user give guess of correct length."""  
    guess: str = input(f"Enter a {str(length)} character word: ")
    while len(guess) != (length):
        if len(guess) != (length):
            print(f"That wasn't {str(length)} chars! Try again: ")
            guess = input("")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turn: int = 1
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess_word: str = input_guess(len(secret))
        print(emojified(secret, guess_word))
        if secret == guess_word:
            print(f"You won in {turn}/6 turns!")
            return
        turn += 1
    if turn > 6:
        print("X/6 - Sorry, try again tomorrow!")
        return


if __name__ == "__main__":
    main()