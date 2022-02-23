"""
Modification mixins extending the traditional chaos game.
"""

import abc
import functools

import chaos.game


class VertexesModification(abc.ABC):
    """
    The base class for mixins which modify the vertexes.
    """

    @abc.abstractmethod
    def get_vertexes(self):
        pass


class NextVertexModification(abc.ABC):
    """
    The base class for mixins which modify the next vertex.
    """

    @abc.abstractmethod
    def get_next_vertex_index(self, selected_vertex_indexes: list[int]):
        pass
