"""Importing + Scope Challenge Question_visualize"""

__author__: str = "730526115"

from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

# create global variables:
x: str = "123"
y: str = "abc"

print(concat(x, y))

get_coords(x, y)
