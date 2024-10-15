"""Summing the elements of a list using different loops"""

__author__: str = "730526115"


# Part 1: w_sum()
def w_sum(vals: list[float]) -> float:
    """A function that adds all items in a list of floats and returns their sum using while loop"""
    index: int = 0
    sum: float = 0.0  # set up the original value for sum
    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum


# Part 2: f_sum
def f_sum(vals: list[float]) -> float:
    """A function that adds all items in a list of floats and returns their sum using for loop"""
    sum: float = 0.0  # set up the original value for sum
    for item in vals:
        sum += item
    return sum


# Part 3: f_range_sum()
def f_range_sum(vals: list[float]) -> float:
    """A function that adds all items in a list of floats and returns their sum using for loop with range"""
    index: int = 0
    sum: float = 0.0
    for index in range(len(vals)):
        sum += vals[index]
        index += 1
    return sum
