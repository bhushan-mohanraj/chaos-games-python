"""
A chaos game that creates the Sierpinski pentagon.
"""

from decimal import Decimal as D

import chaos.game


sierpinski_pentagon_game = chaos.game.Game(
    vertex_count=5,
    point_count=100_000,
    factor=D(2) / (D(1) + D(5).sqrt()),
)
