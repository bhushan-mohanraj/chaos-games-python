"""
A class that represents and runs chaos games.
"""

import random
import functools
from decimal import Decimal as D

import matplotlib.pyplot

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
                chaos.math.get_cos(angle),
                chaos.math.get_sin(angle),
            )

            vertexes.append(vertex)

        return vertexes

    def _get_next_vertex_index(self, vertex_indexes: list[int]) -> int:
        """
        Return the index for the next vertex to jump toward,
        given the list containing the previous vertex indexes.
        """

        return random.randrange(len(self._get_vertexes()))

    @functools.cache
    def _get_points(self) -> list[chaos.point.Point]:
        """
        Generate the points by randomly jumping toward the vertexes
        following the sequence specified by the next-index function.
        """

        points = []

        # The initial point (the origin).
        point = chaos.point.Point()

        # The list of vertex indexes (beginning with the first vertex).
        vertex_indexes = [0]

        for _ in range(self.point_count):
            points.append(point)

            next_vertex = self._get_vertexes()[
                self._get_next_vertex_index(vertex_indexes)
            ]

            point = point * (1 - self.factor) + next_vertex * self.factor

        return points

    def plot(self) -> None:
        """
        Plot the points generated through the chaos game.
        """

        # Set the plot size.
        matplotlib.pyplot.figure(figsize=(12, 12))

        # Plot the points (ignoring the first few).
        matplotlib.pyplot.scatter(
            [float(point.x) for point in self._get_points()][10:],
            [float(point.y) for point in self._get_points()][10:],
            s=1,
        )

        # Style and save the plot.
        # TODO: Use `matplotlib.rcParams` for styling.
        matplotlib.pyplot.axis("off")

        # TODO: Consider adding opacity to markers in the plot.
        matplotlib.pyplot.savefig(
            "game.png",
            pad_inches=0,
        )
