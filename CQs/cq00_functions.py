"""Functions Challenge Question: my first challenge question!"""

__author__ = "730526115"


def mimic(message: str) -> str:
    """Mimic function definition."""
    return message


def main() -> None:
    """Main function definition: pulls together functions in blocks
    into a main function."""
    return print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
# conditional statement: when you run this program in the “Run” tab,
# the indented code beneath the if statement will be evaluated. However,
# when you load this program in the REPL of the “Interact” tab, the code
# beneath the if statement will not be run.
