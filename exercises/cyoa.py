"""CYOA - Rajajoutee the Rat Chef!"""

__author__ = 730555430

player: str = ""
points: int = 0
RAT_CHEF: str = "\U0001F401"
BRUH: str = "\U0001F928"
CAKE: str = "\U0001F370"
player_choice: int = 0


def greet() -> None:
    """Greets user."""
    print(f"Hello user! My name is Rajajoutee.{RAT_CHEF} I love all things cake!!! Say user, what is your name?")
    print("")
    player = input("")
    print(f"Ah. Well. Nice to meet you {player}. Now that you're here, how about asking Ratintoobie {RAT_CHEF} to tell you about cakes hm?")
    print("")


def choice() -> None:
    """Choose the route of the game."""
    global player_choice
    global points

    print(f"(1) Ranjarjuttie! {RAT_CHEF} How do you make a cake?")
    print(f"(2) Rajarjouter! {RAT_CHEF} Cake riddles!")
    print("(3) Nevermind.")

    route: int = int(input("=== Select one by typing 1, 2, or 3 ==="))
    while route != 1 and route != 2 and route != 3:
        print("")
        print(f"On periodt {player}..? -5pts {BRUH} === Select one by typing 1, 2, or 3 === Try again: ")
        points -= 5
        route = int(input())
    if route == 1 or route == 2 or route == 3:
            player_choice = route
            return
    return


def one() -> None:
    """First route in the game."""
    global points
    from random import randint
    print("")
    print("Want to learn how to make a cake? Okay! Press enter.")
    input("")
    print("There are 4 basic ingredients in a cake: milk, sugar, eggs, wheat!")
    print(f"Combine them in the ratio 3:2:1:3, and your cake will be perfect! {CAKE}")
    print("")
    confidence: str = ""
    while confidence != "N" and confidence != "Y":
        confidence: str = input("Sound good? Y/N")
    if confidence == "Y":
        points += 5
        print("(+5pts) Great! Lets test. Input any key to begin.")
    if confidence == "N":
        points -= 5
        print("(-5pts) Oh well! Lets test! Input any key to begin.")

    input("")
    print("===")
    print("I will assign you a random amount of points for each question you get right! We'll go rapid fire so don't worry if you get one wrong. Press Enter.")
    input("")
    print("Question 1: What is my name?")
    input("")
    print("...close enough! Haha just kidding. Let's begin.")
    print(f"Question 1: How many ingredients go into a basic {CAKE}?")

    answer_1: int = int(input(""))
    if answer_1 == 4:
        print("Yes!")
        q1: int = randint(1, 10)
        print(f"+{q1}pts")
        points += q1
    else:
        print("Nope, answer is 4. Next!")
    
    print("")
    print("Question 2: If you have 3 cups of milk, 2 cups of sugar, and 1 egg, how many bundles of wheat should you add? (think: 3:2:1:3)")

    answer_2: int = int(input(""))
    if answer_2 == 3:
        print("Yes!")
        q2: int = randint(1, 10)
        print(f"+{q1}pts")
        points += q2
    else:
        print("Nope, answer is 3. Last question!")
    
    print("")
    print("Question 3: If my recipie calls for 3 eggs, how many cups of milk will I put in?")

    answer_3: int = int(input(""))
    if answer_3 == 9:
        print("Yes!")
        q3: int = randint(1, 10)
        print(f"+{q3}pts")
        points += q3
    else:
        print("Nope! Sorry. Correct answer is 9.")
    print("")
    print("Okay, lets see what you got! Press enter.")
    input("")
    print(f"You now have {points}pts! Press enter.")
    print("===")
    print("Feel free to choose a different route!")


def two(two_points: int) -> int:
    """Second route in the game."""
    from random import randint
    two_points: int
    print(f"Alright! {RAT_CHEF} Now we're going to do cake {CAKE} riddles! Press enter.")
    input("")
    print(f"{RAT_CHEF} I will recite some poetry that matches with different steps of making a cake. Press enter.")
    input("")
    print("Just answer with the letter of the step you think my poetry is referencing! You have 1 chance, so be careful!")
    print("You will get points for each correct answer! Let's get started. Press enter")
    print("===")
    print("")
    input("")

    print("=== Riddle 1 ===")
    print("Strong winds blow the shriveled, lifeless fall leaves...")
    print("Red...yellow...brown...")
    print("Until no longer the colors are distinguishable...")
    print("swirl, wisk, mix...")
    print("===")
    print("")
    print("(a) mix the dry ingredients")
    print("(b) bake at 350 degrees")
    print("(c) Combine wet and dry ingredients")
    print("")
    r1: str = input("")
    if r1 == "a":
        print("Yes!")
        Q1: int = randint(1, 10)
        print(f"+{Q1}pts")
        two_points += Q1
    else:
        print(f"Haha, {RAT_CHEF} better luck next time.")
        print(f"You got {two_points} more pts!")
        return two_points

    print("=== Riddle 2 ===")
    print("Powdery snow falls soft on the tin roof...")
    print("It falls and drifts, and sits and sticks...")
    print("angry with his beak the sparrow does prick...")
    print("at the collection of snow that just seems to grow...")
    print("so he sits on a wire and the winds cools his feathers...")
    print("for the snow took away, his metal tin tray...")
    print("===")
    print("")
    print("(a) Combine wet and dry ingredients.")
    print("(b) Pour the batter into the cake tin.")
    print("(c) Flour the cake tin so the cake wont stick.")
    print("")
    r2: str = input("")
    if r2 == "c":
        print("Yes!")
        Q2: int = randint(1, 10)
        print(f"+{Q2}pts")
        two_points += Q2
    else:
        print(f"Haha, {RAT_CHEF} better luck next time.")
        print(f"You got {two_points} more pts!")
        return two_points

    print("=== Riddle 3 ===")
    print("I thought I was ready, so I took the chance...")
    print("A stab to the heart, the pain when it wrenched...")
    print("I'm grateful however, that I get to see...")
    print("I still need to grow, 'fore I will be me...")
    print("===")
    print("")
    print("(a) Slice the cake")
    print("(b) Stick a toothpick in the center to test doneness.")
    print("(c) Measure the ingredients with a scale.")
    print("")
    r3: str = input("")
    if r3 == "b":
        print("Yes!")
        Q3: int = randint(1, 10)
        print(f"+{Q3}pts")
        two_points += Q3
    else:
        print(f"Haha, {RAT_CHEF} better luck next time.")
        print(f"You got {two_points} more pts!")
        return two_points
    print("===")
    print("")
    print(f"Way to go! You're so much smarter than you look! {RAT_CHEF}")
    print(f"You got {two_points} more pts!")
    return two_points


def main() -> None:
    """Main game loop."""
    global player_choice
    global points
    game_loop: bool = True
    greet()
    while game_loop:
        choice()
        print(f"Alrighty, {player_choice}?")
        
        if player_choice == 3:
            print(f"See you later! {RAT_CHEF}")
            print(f"Points earned: {points}")
            game_loop = False

        if player_choice == 2:
            points += two(points)
            print(f"Total points: {points}")

        if player_choice == 1:
            one()
    quit()


if __name__ == "__main__":
    main()