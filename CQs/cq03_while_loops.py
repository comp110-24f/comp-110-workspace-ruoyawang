"""While Loops Challenge Question"""

__author__: str = "730526115"


def num_instances(phrase: str, search_char: str) -> int:
    """num_instances function: count the occurences of search_char in phrase"""
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1
    print(count)
    return count


num_instances(phrase="HelloHeLloHEllo", search_char="e")
