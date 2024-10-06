"""EX04 - list Utility Functions"""

__author__: str = "730526115"


# Function 1: all
def all(my_list: list[int], num: int) -> bool:
    """A function indicating whether all the ints in the list are the same as the given int"""
    index: int = 0  # set up an index to loop over a list
    condition: bool = True  # prepare for a return in bool
    while index < len(my_list):
        # loop through all items and stop when the index exceeds the total in a list
        if my_list[index] != num:
            condition = False
            return condition
        # short-circuit its behavior and return immediately whenever an item in the list
        # does not match the integer
        else:
            condition = True
            index += 1
        # if still True, run the item of the next index
    if condition == True:
        return condition
    # if True after looping over the list, then all numbers match the indicated number


# Function 2: max
def max(input: list[int]) -> int:
    """A function that returns the largest number in the List"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        index: int = 0  # set up an index to loop over a list
        local_max = input[0]  # the initial largest item
        while index < len(input):
            if input[index] > local_max:
                local_max = input[
                    index
                ]  # mutate the number to be the largest up to that index
            index += 1
    return local_max
    # after looping over the list, the local_max should be the largest of all


# Function 3: is_equal
def is_equal(list0: list[int], list1: list[int]) -> bool:
    """A function that determines if every element at every index is equal in both lists"""
    condition: bool = True  # prepare for a return in bool
    if len(list0) != len(list1):
        condition = False
        return condition
    index: int = 0  # set up an index to loop over a list
    while index < len(list0):
        if (
            list0[index] != list1[index]
        ):  # the index increases at the same time for both lists
            condition = False
            return condition
        # whenever of an index the two items are unequal, returns immediately
        else:
            index += 1
    return condition
    # if still has not returned after conditions and loops, returns True


# Function 4: extend
def extend(list0: list[int], list1: list[int]) -> None:
    """A function that mutates the first list of int values by appending the
    second list's values to the end of it"""
    index: int = 0  # set up an index to loop over a list
    while index < len(list1):
        list0.append(list1[index])  # add the item of each index to the first list
        index += 1
    return None
