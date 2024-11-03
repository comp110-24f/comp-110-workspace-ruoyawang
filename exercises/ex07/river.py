"""File to define River class."""

__author__: str = "730526115"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Situation in the river (of day, fish, and bear)."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Animals should be removed from the River if they are too old."""
        # since I don’t want to be removing things from a list while you’re looping
        # through it, I create new lists and copy all surviving Fish and Bears over to these lists
        new_fish: list[Fish] = []
        new_bears: list[Bear] = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)
        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(bear)
        # update self.fish and self.bears to be equal to that copied list
        self.fish = new_fish
        self.bears = new_bears
        return None

    def remove_fish(self, amount: int):
        """Remove the FRONTMOST Fish."""
        for _ in range(amount):
            # eg. if amount is 3, then it will loop over 0, 1, 2 (3 times) and remove
            # the first item each time
            self.fish.pop(0)

    def bears_eating(self):
        """Each bear eats 3 Fish if there are at least 5 Fish in the river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """If the Bear s starve, remove them from River."""
        # since I don’t want to be removing things from a list while you’re looping
        # through it, I create new lists and copy all surviving Bears over to these lists
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_bears.append(bear)
        # update self.bears to be equal to that copied list
        self.bears = new_bears
        return None

    def repopulate_fish(self):
        """Fish (2) give birth to 4 baby Fish. Add the offspring to the overall Fish population."""
        fish_offspring_num: int = (len(self.fish) // 2) * 4
        # this is only the num! What we add should be object
        for _ in range(fish_offspring_num):
            self.fish.append(Fish())  # add a new Fish object to the self.fish list
        return None

    def repopulate_bears(self):
        """Bear s (2) give birth to 1 baby Bear. Add the offspring to the overall Bear population."""
        bears_offspring_num: int = len(self.bears) // 2
        # this is only the num! What we add should be object
        for _ in range(bears_offspring_num):
            self.bears.append(Bear())  # add a new Bear object to the self.bear list
        return None

    def view_river(self):
        """Print the situation in the river."""
        day_message: str = f"~~~ Day {self.day}: ~~~"
        fish_message: str = f"Fish population: {len(self.fish)}"
        bears_message: str = f"Bear population: {len(self.bears)}"
        print(day_message)
        print(fish_message)
        print(bears_message)
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Call one_river_day() seven times to simulate week."""
        for _ in range(7):
            self.one_river_day()
