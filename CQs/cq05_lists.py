"""Mutating functions."""

__author__: str = "730526115"


# Part1: the first function that append an item to a list:
def manual_append(my_list: list[int], append_num: int) -> None:
    """A function that append the second parameter (append_num) to a list (my_list)"""
    my_list.append(append_num)
    return None


# Part2: the second function that mutates its input by looping through the list and multiplying
# every element in the list[int] parameter by 2:


def double(my_list: list[int]) -> None:
    """A function that loops through the given list and multiplying items by 2"""
    index: int = 0  # index that keep track on the loop
    while index < len(my_list):
        my_list[index] = my_list[index] * 2  # multiply by 2 to double each item
        index += 1
    return None


# Part3: Call double()
list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
# I think both printed results will be [2, 4, 6], as they share the same definition in Heap
# The true results are just as what I expected!
