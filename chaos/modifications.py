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
    A modification which ignores previous vertexes some number of steps ago.
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


# Ignore exact vertex indexes (IgnoreSpecificVertexes).
# Ignore vertex indexes some shift away (IgnoreShiftedVertexes).
# Ignore vertex indexes from some time ago (IgnorePreviousVertexes),
# so that IgnoreTheCurrentVertex subclasses IgnorePreviousVertexes.
