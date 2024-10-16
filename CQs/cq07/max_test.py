"""Unit Test Challenge Question_Test"""

__author__: str = "730526115"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_value() -> None:
    """test fn 1: test if the fn returns the expected value"""
    input: list[int] = [1, 3, 5, 2, 5, 4]
    result: int = find_and_remove_max(input)
    assert result == 5


def test_find_and_remove_max_mutation() -> None:
    """test fn 2: test if the fn mutates the input list correctly"""
    input: list[int] = [1, 3, 5, 2, 5, 4]
    find_and_remove_max(input)
    assert input == [1, 3, 2, 4]


def test_find_and_remove_max_edge() -> None:
    """test fn 3: test if the fn returns the correct value in case of an unconventional input"""
    input: list[int] = []
    result: int = find_and_remove_max(input)
    assert result == -1
