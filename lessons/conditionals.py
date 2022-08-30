SECRET: int = 3

print("Im thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly")
    print("have a wonderful day")
else:
    print("You guessed inorrectly!!!")
    print("Try running the program again")
    if guess > SECRET:
        print("You guessed too high!")
    else:
        print("You guessed too low!")

print("Game over.")
