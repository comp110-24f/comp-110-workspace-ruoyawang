"""EX01 - Tea Party Planner"""

__author__ = "730526115"


def main_planner(guests: int) -> None:
    """A 'main planner' function that calls each and produces printed output."""
    print("A Cozy Tea Party for", guests, "People!")
    print(
        "Tea bags:", tea_bags(people=guests)
    )  # Changing people to guests so they would be in the same format.
    print("Treats:", treats(people=guests))  # Changing people to guests.
    print(
        "Cost: $",  # Q: How to delete the 'blank' between $ and the cost value?
        cost(tea_count=tea_bags(people=guests), treats_count=treats(people=guests)),
    )  # Changing people to guests.


def tea_bags(people: int) -> int:
    """Function for number of tea bags."""
    return people * 2


# Since everyone at the tea party will drink two cups of tea,
# we should plan to have two tea bags for them.


def treats(people: int) -> int:
    """Function for number of treats."""
    tea_count = tea_bags(
        people=people
    )  # * cannot be used for function and float, so have to change the format.
    return int(tea_count * 1.5)  # Calculate the number of treats needed.


# This function assumes for each tea a guest drinks,
# they will want 1.5 treats to eat with it in average.


def cost(tea_count: int, treats_count: int) -> float:
    """Function for the total cost."""
    return tea_count * 0.50 + treats_count * 0.75


# This means each tea bag costs $0.50 and each treat costs $0.75.

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
