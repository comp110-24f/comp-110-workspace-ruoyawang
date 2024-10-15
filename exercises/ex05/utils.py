"""EX05 - `list` Utility Functions"""

__author__: str = "730526115"


# function 1:
def only_evens(
    input: list[int],
) -> list[int]:  # the input contains integers, and what we return
    # should be some integers within the list, so we should also return a list of integers
    """returns a new list containing only the elements of the input list that were even"""
    new_list: list[int] = []  # initializing an empty list
    for item in input:
        if (
            item % 2 == 0
        ):  # the even numbers are those that are divisible by 2 with no remainder
            new_list.append(item)
    return new_list


# function 2:
def sub(
    input: list[int], start_index: int, end_index: int
) -> list[int]:  # since we return
    # a subset of input, the list we return should also be of integers
    """creates a subset of the input list between the specified start index and the end index - 1"""
    new_list: list[int] = []  # initializing an empty list
    for (
        item
    ) in (
        input
    ):  # I previously tried while loop but it seems I cannot loop over the beginning items
        # if the start_index is larger than 0, so only for can be used
        if input.index(item) >= start_index and input.index(item) <= end_index - 1:
            new_list.append(item)
    return new_list


# function 3:
def add_at_index(input: list[int], element: int, index: int) -> None:
    """modifies the input list to place the element at the given index"""
    if index < 0 or index > len(input):
        raise IndexError("Index is out of bounds for the input list")
    input.append(0)  # add a space to the end
    current_index = len(input) - 1  # shift from the last index to the wanted index
    while current_index > index:
        input[current_index] = input[current_index - 1]
        current_index -= 1  # for example, if the list is [1, 2, 4, 5, 0]
        # and the current_index is 4, which is of "0", input[4] = input[4 - 1] = 5, meaning the list
        # is now [1, 2, 4, 5, 5]. Then we loop over current_index 3, making the list [1, 2, 4, 4, 5].
        # if our wanted index == current_index, which is 2 for example, the loop will not run, and we
        # will have the following (element is 3):
    input[index] = (
        element  # which will be input[2] = 3. This will mutate that of index 2 directly and
    )
    # what we have now is [1, 2, 3, 4, 5]
