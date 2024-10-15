"""EX05 - `list` Utility Functions"""

__author__: str = "730526115"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


# only evens:
def test_only_even_edge_all_odds() -> None:
    """edge case for only_evens: all numbers are odd"""
    assert only_evens(input=[1, 3, 5, 7]) == []


def test_only_evens_1_mixture() -> None:
    """1st case for only_evens: normal list of a mixture of odds and evens"""
    assert only_evens(input=[1, 2, 3, 4, 5]) == [2, 4]


def test_only_evens_2_all_same_evens() -> None:
    """2nd case for only_evens: all the same evens"""
    assert only_evens(input=[2, 2, 2, 2]) == [2, 2, 2, 2]


# sub:
def test_sub_edge_empty_list() -> None:
    """edge case for sub: list is empty"""
    list0 = []
    assert sub(list0, 2, 6) == []


def test_sub_1_positive_index() -> None:
    """1st case for sub: a positive index"""
    a_list = [10, 30, 50, 70, 90]
    assert sub(a_list, 1, 4) == [30, 50, 70]


def test_sub_2_negative_start_index_and_great_end_index() -> None:
    """2nd case for sub: a negative start index and an end index greater than the length of the list"""
    a_list = [2, 3, 4, 5]
    assert sub(a_list, -2, 8) == [2, 3, 4, 5]
    # If the start index is negative, start from the beginning of the list.
    # If the end index is greater than the length of the list, end with the end of the list.


# add at index:


def test_add_at_index_edge_empty_list() -> None:
    """edge case for add at index: list is empty and will raise an IndexError for an invalid index"""
    list0 = []
    with pytest.raises(IndexError):
        add_at_index(list0, 2, 3)


def test_add_at_index_1_normal_list() -> None:
    """1st case for add at index: normal list"""
    list1 = [1, 2, 4, 5]
    add_at_index(list1, 3, 2)
    assert list1 == [1, 2, 3, 4, 5]


def test_add_at_index_2_only_one_item() -> None:
    """2nd case for add at index: list with only 1 item"""
    list2 = [4]
    add_at_index(list2, 5, 1)
    assert list2 == [4, 5]
