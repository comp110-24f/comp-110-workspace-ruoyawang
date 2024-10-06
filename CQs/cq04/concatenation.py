"""Importing + Scope Challenge Question_concatenation"""

__author__ = "730526115"


def concat(string1: str, string2: str) -> str:
    """The function returns the concatenation of the two input strings"""
    concatenation = string1 + string2
    return concatenation


# Two global variables:
word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":
    print(concat(word1, word2))
