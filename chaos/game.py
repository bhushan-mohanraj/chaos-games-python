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

    # The modification classes,
    # which should override the vertex or next-vertex functions.
    modifications: list[type] = []

    @functools.cache
    def get_vertexes(self) -> list[chaos.point.Point]:
        """
        Calculate the vertexes to jump toward.
        By default, these are the initial polygon vertexes.
        """

        for modification in self.modifications:
            if hasattr(modification, "get_vertexes"):
                return modification.get_vertexes(self)

        vertexes = []

        for i in range(self.vertex_count):
            angle = 2 * chaos.math.PI * i / self.vertex_count

            vertex = chaos.point.Point(
                chaos.math.get_cos(angle),
                chaos.math.get_sin(angle),
            )

            vertexes.append(vertex)

        return vertexes

    def get_next_vertex_index(self, selected_vertex_indexes: list[int]) -> int:
        """
        Return the index for the next vertex to jump toward,
        given the list containing the previous vertex indexes.
        """

        for modification in self.modifications:
            if hasattr(modification, "get_next_vertex_index"):
                return modification.get_next_vertex_index(self, selected_vertex_indexes)

        return random.randrange(len(self.get_vertexes()))

    @functools.cache
    def get_points(self) -> list[chaos.point.Point]:
        """
        Generate the points by randomly jumping toward the vertexes
        following the sequence specified by the next-index function.
        """

        points = []

        # The initial point (the origin).
        point = chaos.point.Point()

        # The vertex indexes selected to jump toward.
        selected_vertex_indexes = [0]

        for _ in range(self.point_count):
            points.append(point)

            next_vertex_index = self.get_next_vertex_index(selected_vertex_indexes)
            selected_vertex_indexes.append(next_vertex_index)

            next_vertex = self.get_vertexes()[next_vertex_index]

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
            [float(point.x) for point in self.get_points()][10:],
            [float(point.y) for point in self.get_points()][10:],
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
