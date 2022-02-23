from decimal import Decimal as D

import chaos.game


class SierpinskiTriangleGame(chaos.game.Game):
    vertex_count = 3
    point_count = 100_000
    factor = D(1) / D(2)


class SierpinskiPentagonGame(chaos.game.Game):
    vertex_count = 5
    point_count = 100_000
    factor = D(2) / (D(1) + D(5).sqrt())
