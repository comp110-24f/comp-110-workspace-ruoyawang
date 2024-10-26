"""EX06 - Dictionary Utility Functions"""

__author__: str = "730526115"


# invert
def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """the function returns a dictionary that inverts the keys and the values"""
    new_dict: dict[str, str] = {}  # creating a new dictionary to add keys and values
    for key in input_dict:  # for loop that goes through all keys in input_dict
        if input_dict[key] in new_dict:  # if have identical values
            raise KeyError("error message of your choice here!")
        new_dict[input_dict[key]] = key
    # input_dict[key] is value, and new_dict[value] adds value as key and regards the
    # previous key as value
    return new_dict


# favorite color
def favorite_color(names_and_colors_dict: dict[str, str]) -> str:
    """the function takes in names and favorite colors and returns the color that appears most frequently"""
    color_count: dict[str, int] = (
        {}
    )  # a new dict with color as key and frequency as value
    for name in names_and_colors_dict:
        color = names_and_colors_dict[name]
        # create the key "color", which is originally the value in names_and_colors_dict
        if color in color_count:
            color_count[color] += 1  # if one color reoccur, its frequency is added by 1
        else:
            color_count[color] = (
                1  # when we encounter the first color, its frequency is 1
            )
    max_count: int = 0
    most_freq_color: str = ""  # initializing two variables
    for color in color_count:
        if color_count[color] > max_count:
            # it will only count the first color with a frequency larger than previous
            # max_count. If there is a color with the same frequency it will not be counted
            most_freq_color = color  # update the most frequent color
            max_count = color_count[color]  # and also the frequency
    return most_freq_color


# count
def count(input_list: list[str]) -> dict[str, int]:
    """the function returns a dict where each key is a unique value in the given list and each
    value associated is the count of the number of times that value appeared in the input list.
    """
    new_dict: dict[str, int] = {}
    for i in input_list:  # i is the value in the input_list
        if i in new_dict:
            new_dict[i] += 1
        # If the item is found in the dict, the pair of that specific key and value exist so we only update it
        else:
            new_dict[i] = 1
        # initialize the dict as it is the first time we encounter that item
    return new_dict


# alphabetizer
def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """the function returns a dict where each key is a unique letter in the alphabet and
    each value is a list of the words that begin with that letter."""
    new_dict: dict[str, list[str]] = {}  # initialize a dict
    for i in input_list:  # i here is the item (word) in input_list
        first_char: str = i[0]  # this extracts the first character of the item
        if (
            first_char in new_dict
        ):  # if the first character has already been initialized as a key in dict
            new_dict[first_char.lower()].append(i)
            # then we can simply add values to the list as the value of the dict
        else:
            new_dict[first_char.lower()] = [
                i
            ]  # if not, we initialize the key paired with the first value in a list
    return new_dict


# update attendance
def update_attendance(input_dict: dict[str, list[str]], day: str, student: str) -> None:
    """this function mutates and returns the input dictionary"""
    if day in input_dict:  # day of a week as key of input_dict. If it is already there
        if (
            student not in input_dict[day]
        ):  # to ensure the same student is not added twice
            input_dict[day].append(
                student
            )  # then we add student directly to the list as the value of dict
    else:  # if the day is not there, we should initialize one
        input_dict[day] = [
            student
        ]  # the new key(day) will pair with a student name for the first time
    return None
