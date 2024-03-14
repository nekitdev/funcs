from typing import TypeVar, Union

from solus import Singleton
from typing_extensions import TypeIs

__all__ = ("Marker", "MarkerOr", "marker", "is_marker")

T = TypeVar("T")


class Marker(Singleton):
    """Represents markers used in various checks."""


marker = Marker()
"""The instance of [`Marker`][funcs.types.Marker]."""

MarkerOr = Union[Marker, T]
"""The union of [`Marker`][funcs.types.Marker] and `T`."""


def is_marker(item: MarkerOr[T]) -> TypeIs[Marker]:
    """Checks if the given `item` is [`marker`][funcs.types.marker].

    Arguments:
        item: The item to check.

    Returns:
        Whether the given `item` is [`marker`][funcs.types.marker].
    """
    return item is marker
