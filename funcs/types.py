from typing import Any, TypeVar, Union

from solus import Singleton
from typing_extensions import TypeGuard

__all__ = ("Marker", "MarkerOr", "marker", "is_marker", "is_not_marker")

T = TypeVar("T")


class Marker(Singleton):
    """Represents the marker type."""


marker = Marker()

MarkerOr = Union[Marker, T]


def is_marker(item: Any) -> TypeGuard[Marker]:
    return item is marker


def is_not_marker(item: MarkerOr[T]) -> TypeGuard[T]:
    return item is not marker
