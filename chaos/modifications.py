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

    def __init__(self):
        """
        Initialize the modification.

        Subclasses should override this method
        for implementing customization.
        """

    def get_vertexes(self):
        raise NotImplementedError

    def get_next_vertex_index(self, selected_vertex_indexes: list[int]):
        raise NotImplementedError


class VertexesModification(abc.ABC):
    """
    The base class for mixins which modify the vertexes.
    """

    @abc.abstractmethod
    def get_vertexes(self):
        pass

    def get_next_vertex_index(self, selected_vertex_indexes: list[int]):
        raise NotImplementedError


class NextVertexModification(abc.ABC):
    """
    The base class for mixins which modify the next vertex.
    """

    def get_vertexes(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_next_vertex_index(self, selected_vertex_indexes: list[int]):
        pass


class IgnoreTheCurrentVertexModification(NextVertexModification):
    """
    A modification which ignores the current vertex
    when selecting the next one.
    """

    def get_next_vertex_index(self, selected_vertex_indexes: list[int]) -> int:
        """
        Choose from the vertexes at random,
        but ignore the current vertex.
        """

        current_vertex_index = selected_vertex_indexes[-1]

        vertex_indexes = list(range(len(self.get_vertexes())))
        vertex_indexes.remove(current_vertex_index)

        return random.choice(vertex_indexes)


# Ignore exact vertex indexes (IgnoreSpecificVertexes).
# Ignore vertex indexes some shift away (IgnoreShiftedVertexes).
# Ignore vertex indexes from some time ago (IgnorePreviousVertexes),
# so that IgnoreTheCurrentVertex subclasses IgnorePreviousVertexes.
