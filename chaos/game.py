"""
A class that represents and runs chaos games.
"""

import random
import functools
from decimal import Decimal as D

import chaos.math
import chaos.point


class Game:
    """
    A chaos game.
    """

    # The vertexes for the intial polygon.
    vertex_count = 3

    # The points to generate by jumping toward the vertexes.
    point_count = 1000

    # The fraction of the distance to jump toward each vertex.
    factor = D(1) / D(2)

    @functools.cache
    def _get_vertexes(self) -> list[chaos.point.Point]:
        """
        Calculate the vertexes to jump toward.
        By default, these are the initial polygon vertexes.
        """

        vertexes = []

        for i in range(self.vertex_count):
            angle = 2 * chaos.math.PI * i / self.vertex_count

            vertex = chaos.point.Point(
                chaos.math.cos(angle),
                chaos.math.sin(angle),
            )

            vertexes.append(vertex)

        return vertexes

    def _get_next_vertex_index(self, vertex_indexes: list[int]) -> int:
        """
        Return the index for the next vertex to jump toward,
        given the list containing the previous vertex indexes.
        """

        return random.randrange(len(self._get_vertexes()))
