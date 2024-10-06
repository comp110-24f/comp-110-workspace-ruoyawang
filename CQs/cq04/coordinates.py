"""Importing + Scope Challenge Question_coordinates"""

__author__: str = "730526115"


def get_coords(xs: str, ys: str) -> None:
    x_index: int = 0
    y_index: int = 0

    while x_index < len(xs):
        while y_index < len(ys):
            print("(" + xs[x_index] + "," + ys[y_index] + ")")
            y_index += 1
        x_index += 1
        y_index = 0
    return None
