"""
Chaos games for squares.
"""

from decimal import Decimal as D

import chaos.game
import chaos.modifications


square_1_game = chaos.game.Game(
    vertex_count=4,
    point_count=100_000,
    factor=D(1) / D(2),
    modifications=[
        chaos.modifications.IgnoreShiftedVertexesModification([2]),
    ],
)

square_2_game = chaos.game.Game(
    vertex_count=4,
    point_count=100_000,
    factor=D(1) / D(2),
    modifications=[
        chaos.modifications.IgnorePreviousVertexesModification([-1]),
    ],
)

square_3_game = chaos.game.Game(
    vertex_count=4,
    point_count=100_000,
    factor=D(1) / D(2),
    modifications=[
        chaos.modifications.IgnoreShiftedVertexesModification([1]),
    ],
)
