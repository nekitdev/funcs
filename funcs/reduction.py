from functools import reduce as standard_reduce
from typing import Iterable, TypeVar

from typing_aliases import Binary

__all__ = ("reduce", "fold")

T = TypeVar("T")
U = TypeVar("U")


def reduce(function: Binary[T, T, T], iterable: Iterable[T]) -> T:
    """Reduces the given `iterable` using the `function`.

    Example:
        ```python
        from operator import add

        from funcs.reduction import reduce

        print(reduce(add, [1, 2, 3, 4, 5]))  # 15
        ```

    Arguments:
        function: The function to use in reduction.
        iterable: The iterable to reduce.

    Returns:
        The reduced value.
    """
    return standard_reduce(function, iterable)


def fold(initial: U, function: Binary[U, T, U], iterable: Iterable[T]) -> U:
    """Folds the given `iterable` using the `function` and the `initial` value.

    Arguments:
        initial: The initial value to use in folding.
        function: The function to use in folding.
        iterable: The iterable to fold.

    Returns:
        The folded value.
    """
    return standard_reduce(function, iterable, initial)
