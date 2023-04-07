from operator import methodcaller as method_caller
from typing import Any, TypeVar

from typing_extensions import ParamSpec

from funcs.typing import DynamicCallable, Unary

__all__ = ("caller", "method_caller")

P = ParamSpec("P")

R = TypeVar("R")


def caller(*args: Any, **kwargs: Any) -> Unary[DynamicCallable[R], R]:
    def call(function: DynamicCallable[R]) -> R:
        return function(*args, **kwargs)

    return call
