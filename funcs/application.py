from functools import partial
from typing import Callable, TypeVar

from typing_extensions import ParamSpec

__all__ = ("apply", "partial")

P = ParamSpec("P")
R = TypeVar("R")


def apply(function: Callable[P, R], *args: P.args, **kwargs: P.kwargs) -> R:
    return function(*args, **kwargs)
