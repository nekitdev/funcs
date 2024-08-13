from __future__ import annotations

from typing import Any, TypeVar, Union

from solus import Singleton
from typing_extensions import TypeIs

T = TypeVar("T")


class Marker(Singleton):
    pass


marker = Marker()

MarkerOr = Union[Marker, T]


def is_marker(item: Any) -> TypeIs[Marker]:
    return item is marker
