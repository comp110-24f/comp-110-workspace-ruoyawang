"""File to define Fish class."""

__author__: str = "730526115"


class Fish:
    """Fish living in the river."""

    age: int

    def __init__(self):
        """Initializing self.age with the value 0."""
        self.age = 0
        return None

    def one_day(self):
        """Increase the value of the age attribute by 1."""
        self.age += 1
        return None
