"""
Modification mixins extending the traditional chaos game.
"""

import abc
import random
import functools


class VertexesModification(abc.ABC):
    """
    The base class for mixins which modify the vertexes.
    """

    @abc.abstractmethod
    def get_vertexes(self):
        pass

    @abc.abstractmethod
    def get_next_vertex_index(self, selected_vertex_indexes: list[int]):
        pass


class NextVertexModification(abc.ABC):
    """
    The base class for mixins which modify the next vertex.
    """

    @abc.abstractmethod
    def get_vertexes(self):
        pass

    @abc.abstractmethod
    def get_next_vertex_index(self, selected_vertex_indexes: list[int]):
        pass


class IgnoreTheCurrentVertex(NextVertexModification):
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
