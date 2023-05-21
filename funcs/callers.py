from operator import methodcaller as standard_method_caller
from typing import Any, TypeVar

from typing_aliases import DynamicCallable, Unary
from typing_extensions import ParamSpec

__all__ = ("caller", "method_caller")

method_caller = standard_method_caller
"""An alias of the standard `method_caller` type that implements method calling."""

P = ParamSpec("P")

R = TypeVar("R")


def caller(*args: Any, **kwargs: Any) -> Unary[DynamicCallable[R], R]:
    """Creates a function that calls the given `function` with `*args` and `**kwargs`.

    Arguments:
        *args: The arguments to use.
        **kwargs: The keyword arguments to use.

    Returns:
        The function that calls the given `function` with `*args` and `**kwargs`.
    """

    def call(function: DynamicCallable[R]) -> R:
        return function(*args, **kwargs)

    return call
