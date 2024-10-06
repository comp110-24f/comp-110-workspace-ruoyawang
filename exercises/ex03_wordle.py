"""EX03 - Structured Wordle"""

__author__: str = "730526115"


def input_guess(secret_word_len: int) -> str:
    """input_guess function: evaluates if the length of the input word is proper"""
    word = input(f"Enter a {secret_word_len} character word: ")
    while len(word) != secret_word_len:
        # we should loop the != instead of == as we demand modification of the word
        # when it is not of the correct length
        word = input(
            f"That wasn't {secret_word_len} chars! Try again: "
        )  # Using f-string template!
    return word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """contains_char function: tests each index of the secret_word to see if it matches
    the char_guess"""
    assert len(char_guess) == 1
    index: int = 0
    while index < len(secret_word):
        # here we have the first while loop; it will stop if the index is equal or
        # larger than the word length
        while secret_word[index] == char_guess:
            # here is the second loop; as index gets higher, it will go through each
            # chars in word in sequence and return True if criteria is met
            return True
            # immediately exit the function once a match is found
        index += 1
    return False
    # only printed if the entire word has been checked and no match is found


def emojified(guess: str, secret: str) -> str:
    """emojified function: emojifies the guess characters' absence, presence, and
    position compared to secret"""
    assert len(guess) == len(secret)
    # local variables:
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result: str = ""
    index: int = 0
    # a loop similar to that in contains_char
    while index < len(secret):
        if guess[index] == secret[index]:
            # If the character at the current index of the guess word matches the
            # character at the same index
            result += GREEN_BOX
        elif contains_char(secret, guess[index]):
            # if the character of the guess word is present in the secret word
            result += YELLOW_BOX
            # the character at the current index in the guess word is not present
        else:
            result += WHITE_BOX
        index += 1
        # the index += 1 should be inside the while loop or it will not loop
    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1  # state of the game that we keeps track on
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))  # using input_guess function
        result: str = emojified(guess, secret)  # using emojified function
        print(result)
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            return (
                None  # again, this makes it possible to immediately exit the function
            )
        turn += (
            1  # this is still in while loop; if condition in "if" isn't met it will run
        )
    print("X/6 - Sorry, try again tomorrow!")  # this should not be in the while loop!


if __name__ == "__main__":
    main(secret="codes")
