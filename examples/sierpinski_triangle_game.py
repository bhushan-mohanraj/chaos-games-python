"""
A chaos game that creates the Sierpinski triangle.
"""

import pathlib
from decimal import Decimal as D

import chaos.game


class SierpinskiTriangleGame(chaos.game.Game):
    """
    A chaos game that creates the Sierpinski triangle.
    """

    vertex_count = 3
    point_count = 100_000
    factor = D(1) / D(2)

    path = pathlib.Path(__file__).with_suffix(".png")
