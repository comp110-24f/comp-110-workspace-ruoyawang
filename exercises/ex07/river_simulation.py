"""EX07 - River Simulation."""

__author__: str = "730526115"

from exercises.ex07.river import River

my_river: River = River(10, 2)
my_river.view_river()

# One week in the river
my_river.one_river_week()
