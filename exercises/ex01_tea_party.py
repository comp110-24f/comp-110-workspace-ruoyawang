"""EX01 - Tea Party Planner"""

__author__: str = "730526115"


def main_planner(guests: int) -> None:
    """A 'main planner' function that calls each and produces printed output."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print(
        "Tea bags: " + str(tea_bags(guests))
    )  # Changing people to guests so they would be in the same format.
    print("Treats: " + str(treats(guests)))  # Changing people to guests.
    print(
        "Cost: $" + str(cost(tea_bags(guests), treats(guests)))
    )  # Changing people to guests.


def tea_bags(people: int) -> int:
    """Function for number of tea bags."""
    return people * 2


# Since everyone at the tea party will drink two cups of tea,
# we should plan to have two tea bags for them.


def treats(people: int) -> int:
    """Function for number of treats."""
    return int(tea_bags(people=people) * 1.5)  # Calculate the number of treats needed.


# This function assumes for each tea a guest drinks,
# they will want 1.5 treats to eat with it in average.


def cost(tea_count: int, treats_count: int) -> float:
    """Function for the total cost."""
    return tea_count * 0.50 + treats_count * 0.75


# This means each tea bag costs $0.50 and each treat costs $0.75.

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
