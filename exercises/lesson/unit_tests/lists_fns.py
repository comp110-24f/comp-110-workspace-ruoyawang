def get_first(input: list[str]) -> str:
    """Returns the first element in the list"""
    item: str = input[0]
    return item


def remove_first(input: list[str]) -> None:
    """Pop the first element off of input list"""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """Return first element and pops it off"""
    first: str = input[0]
    input.pop(0)
    return first
