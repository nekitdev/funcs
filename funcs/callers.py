from operator import methodcaller as standard_method_caller
from typing import Any, TypeVar

from attrs import frozen
from typing_aliases import DynamicCallable, DynamicTuple, StringDict, Unary
from typing_extensions import ParamSpec, final

__all__ = ("caller", "method_caller")

method_caller = standard_method_caller
"""An alias of the standard `method_caller` type that implements method calling."""

P = ParamSpec("P")

R = TypeVar("R")


@final
@frozen()
class Caller:
    """Represents function callers."""

    args: DynamicTuple[Any]
    kwargs: StringDict[Any]

    def __call__(self, function: DynamicCallable[R]) -> R:
        return function(*self.args, **self.kwargs)


def caller(*args: Any, **kwargs: Any) -> Unary[DynamicCallable[R], R]:
    """Creates a [`Caller`][funcs.callers.Caller] that calls the given
    `function` with `*args` and `**kwargs`.

    Arguments:
        *args: The arguments to use.
        **kwargs: The keyword arguments to use.

    Returns:
        The [`Caller`][funcs.callers.Caller] created.
    """
    return Caller(args, kwargs)
