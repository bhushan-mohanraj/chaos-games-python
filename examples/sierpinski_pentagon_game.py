"""
A chaos game that creates the Sierpinski pentagon.
"""

import pathlib
from decimal import Decimal as D

import chaos.game


class SierpinskiPentagonGame(chaos.game.Game):
    """
    A chaos game that creates the Sierpinski pentagon.
    """

    vertex_count = 5
    point_count = 100_000
    factor = D(2) / (D(1) + D(5).sqrt())

    path = pathlib.Path(__file__).with_suffix(".png")
