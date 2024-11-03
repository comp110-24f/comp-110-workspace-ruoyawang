"""File to define Bear class."""

__author__: str = "730526115"


class Bear:
    """Bears living by the river."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes both self.age and hunger_score with the value 0."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Increase the value of the age attribute by 1."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Increase the Bear's hunger_score (increases by num_fish)."""
        self.hunger_score += num_fish
