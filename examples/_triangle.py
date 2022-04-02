"""
Chaos games for triangles.
"""

from decimal import Decimal as D

import chaos.game


triangle_sierpinski_game = chaos.game.Game(
    vertex_count=3,
    point_count=100_000,
    factor=D(1) / D(2),
)
