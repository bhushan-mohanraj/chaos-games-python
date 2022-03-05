"""
Modification mixins extending the traditional chaos game.
"""

import abc
import random
import functools


class Modification(abc.ABC):
    """
    The base class for modification mixins.
    """

    # The game which this modification modifies.
    # The game instance sets this attribute for each modification.
    game = None

    def __init__(self):
        """
        Initialize the modification.

        Subclasses should override this method
        for implementing customization.
        """


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


class IgnoreTheCurrentVertexModification(NextVertexModification):
    """
    A modification which ignores the current vertex
    when selecting the next one.
    """

    def get_next_vertex_index(self) -> int:
        """
        Choose from the vertexes at random,
        but ignore the current vertex.
        """

        current_vertex_index = self.game.selected_vertex_indexes[-1]

        vertex_indexes = list(range(len(self.game.get_vertexes())))
        vertex_indexes.remove(current_vertex_index)

        return random.choice(vertex_indexes)


# Ignore exact vertex indexes (IgnoreSpecificVertexes).
# Ignore vertex indexes some shift away (IgnoreShiftedVertexes).
# Ignore vertex indexes from some time ago (IgnorePreviousVertexes),
# so that IgnoreTheCurrentVertex subclasses IgnorePreviousVertexes.
