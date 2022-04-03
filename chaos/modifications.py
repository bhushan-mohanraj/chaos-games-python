"""
Modification mixins extending the traditional chaos game.
"""

import abc
import random
import functools


class Modification(abc.ABC):
    """
    The base class for modification mixins.

    Subclasses should override the initialization method
    to implement customization of the modification.
    """

    # The game which this modification modifies.
    # The game instance sets this attribute for each modification.
    game = None


class VertexesModification(Modification):
    """
    The base class for mixins which modify the vertexes.
    """

    @abc.abstractmethod
    def get_vertexes(self):
        pass


class NextVertexModification(Modification):
    """
    The base class for mixins which modify the next vertex.
    """

    @abc.abstractmethod
    def get_next_vertex_index(self):
        pass


class IgnorePreviousVertexesModification(NextVertexModification):
    """
    A modification which ignores vertexes selected some number of steps ago.
    """

    # The steps ago of the ignored vertexes, represented as negative integers.
    # For example, if the list has negative one, the last vertex is ignored.
    ignored_steps: list[int] = []

    def __init__(self, ignored_steps: list[int]):
        """
        Customize the ignored steps.
        """

        self.ignored_steps = ignored_steps

    def get_next_vertex_index(self) -> int:
        """
        Choose from the vertexes at random,
        but ignore certain previous vertexes.
        """

        assert len(self.ignored_steps) < len(self.game.get_vertexes()), (
            "The number of potentially-ignored vertexes"
            " must be less than the number of total vertexes."
        )

        vertex_indexes = list(range(len(self.game.get_vertexes())))

        for ignored_step in self.ignored_steps:
            if -len(self.game.selected_vertex_indexes) <= ignored_step < 0:
                ignored_vertex_index = self.game.selected_vertex_indexes[ignored_step]

                while ignored_vertex_index in vertex_indexes:
                    vertex_indexes.remove(ignored_vertex_index)

        return random.choice(vertex_indexes)


class IgnoreShiftedVertexesModification(NextVertexModification):
    """
    A modification which ignores vertexes shifted from the current vertex.
    """

    # The shifts of the ignored vertexes, represented
    # as positive (counterclockwise) or negative (clockwise) integers.
    ignored_shifts: list[int] = []

    def __init__(self, ignored_shifts: list[int]):
        """
        Customize the modification.
        """

        self.ignored_shifts = ignored_shifts

    def get_next_vertex_index(self) -> int:
        """
        Choose from the vertexes at random, but ignore some shifted vertexes.
        """

        current_vertex_index = self.game.selected_vertex_indexes[-1]
        vertex_indexes = list(range(len(self.game.get_vertexes())))

        assert len(self.ignored_shifts) < len(vertex_indexes), (
            "The number of ignored vertexes"
            " must be less than the total number of vertexes."
        )

        for ignored_shift in self.ignored_shifts:
            ignored_vertex_index = current_vertex_index + ignored_shift
            ignored_vertex_index %= len(vertex_indexes)

            while ignored_vertex_index in vertex_indexes:
                vertex_indexes.remove(ignored_vertex_index)

        return random.choice(vertex_indexes)
