"""
A class that represents and runs chaos games.
"""

import decimal

import chaos.math


class ChaosGame:
    """
    A chaos game.
    """

    # The vertexes for the intial polygon.
    vertex_count = 3

    # The points to generate by jumping to the vertexes.
    point_count = 1000

    # The fraction of the distance to jump to each vertex.
    factor = 1 / 2
