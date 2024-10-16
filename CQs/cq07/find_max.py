"""Unit Test Challenge Question"""

__author__: str = "730526115"


def find_and_remove_max(input: list[int]) -> int:
    """finds and return the largest number in the input list"""
    if input == []:
        return -1  # for the case when input is an empty list
    else:
        largest_num: int = input[0]  # start with the first item
        for item in input:  # more convenient using for loop here
            if item > largest_num:
                largest_num = item  # mutate largest_num with the larger number
        index: int = 0
        while index < len(input):
            if input[index] == largest_num:
                input.pop(index)
            # pop out every largest nums; works when we have two identical numbers in
            # a list that are both the laargest
            else:
                index += 1
    return largest_num
