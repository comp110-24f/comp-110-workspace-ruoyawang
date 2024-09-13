"""Practice with Conditionals, Local Variables, and User Input"""

__author__: str = "730526115"


def guess_a_number(x: int) -> None:
    secret: int = 7
    x = int(input("Guess a number:"))
    print("Your guess was " + str(x))
    if x < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    elif x > secret:
        print("Your guess was too high! The secret number is " + str(secret))
    else:
        print("You got it!")
    return None


if __name__ == "__main__":
    guess_a_number()
