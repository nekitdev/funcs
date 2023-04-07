from functools import reduce as standard_reduce
from typing import Iterable, TypeVar

from funcs.typing import Binary

__all__ = ("reduce", "fold")

T = TypeVar("T")
U = TypeVar("U")

REDUCE_ON_EMPTY = "reduce() called on an empty iterable"


def reduce(function: Binary[T, T, T], iterable: Iterable[T]) -> T:
    return standard_reduce(function, iterable)


def fold(initial: U, function: Binary[U, T, U], iterable: Iterable[T]) -> U:
    return standard_reduce(function, iterable, initial)
