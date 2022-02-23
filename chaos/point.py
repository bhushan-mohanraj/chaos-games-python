"""
A class for creating and manipulating 2D points.
"""

from decimal import Decimal as D


class Point:
    """
    A 2D point.
    """

    def __init__(self, x: D = D(0), y: D = D(0)):
        """
        Create the point, which default to the origin.
        """

        assert isinstance(x, D)
        assert isinstance(y, D)

        self.x = x
        self.y = y

    def __add__(self, other):
        """
        Add two points with vector addition.
        """

        assert isinstance(other, Point)

        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        Subtract two points with vector subtraction.
        """

        assert isinstance(other, Point)

        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """
        Multiply the point by a scalar.
        """

        assert isinstance(other, (int, float, D))

        return Point(self.x * other, self.y * other)

    def __rmul__(self, other):
        """
        Multiply the point by a scalar.
        """

        return self * other
