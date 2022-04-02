"""
Chaos games for pentagons.
"""

from decimal import Decimal as D

import chaos.game


pentagon_sierpinski_game = chaos.game.Game(
    vertex_count=5,
    point_count=100_000,
    factor=D(2) / (D(1) + D(5).sqrt()),
)
