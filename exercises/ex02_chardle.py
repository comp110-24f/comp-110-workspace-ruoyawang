"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "1234567890"


def input_word() -> str:  # no parameter and return a string
    input_from_user: str = input("Enter a 5-character word: ")
    if (
        len(input_from_user) != 5
    ):  # If a length of 5 is not satisfied, the function will print error first
        print("Error: Word must contain 5 characters.")
        exit()
    # exit() should be added here with indentation as the program quits only if the length is not 5
    # Also, it should be after print(), or print() will not run
    return input_from_user


def input_letter() -> str:  # no parameter and return a string
    input_from_user1: str = input("Enter a single character: ")
    if (
        len(input_from_user1) != 1
    ):  # If a length of 1 is not satisfied, the function will print error first
        print("Error: Character must be a single character.")
        exit()
    # exit() should be added here with indentation as the program quits only if the length is not 1
    # Also, it should be after print(), or print() will not run
    return input_from_user1


def contains_char(word: str, letter: str) -> None:  # two parameters returns none
    print("Searching for " + letter + " in " + word)
    count: int = 0
    # I would like the count to start as 0 so every time the letter appears in word
    # it will increase in number
    if letter in word:
        if letter == word[0]:
            print(letter + " found at index 0")
            count += 1
        if letter == word[1]:
            print(letter + " found at index 1")
            # we should not use elif here as it will stop counting after encountering the first
            # condition it satisfies
            count += 1
        if letter == word[2]:
            print(letter + " found at index 2")
            count += 1
        if letter == word[3]:
            print(letter + " found at index 3")
            count += 1
        if letter == word[4]:
            print(letter + " found at index 4")
            count += 1
    if count == 1:
        # This evaluation of count value should be put after all our addings, otherwise the count will
        # not be updated
        print(str(count) + " instance of " + letter + " found in " + word)
    elif count > 1:
        print(str(count) + " instances of " + letter + " found in " + word)
    else:
        print("No instance of " + letter + " found in " + word)
    # These are the three expressions


def main() -> None:  # automatically handles all the function calls
    return contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
