from __future__ import annotations

from functools import partial as standard_partial
from typing import Any, Callable, Tuple, TypeVar, overload

from typing_aliases import DynamicCallable, DynamicTuple, EmptyTuple
from typing_extensions import ParamSpec

__all__ = ("apply", "juxt", "partial")

P = ParamSpec("P")
R = TypeVar("R")

partial = standard_partial
"""An alias of the standard `partial` type that implements partial application."""


def apply(function: Callable[P, R], *args: P.args, **kwargs: P.kwargs) -> R:
    """Applies the `function` to given positional and keyword arguments.

    ```python
    apply(function, *args, **kwargs)
    ```

    Is identical to:

    ```python
    function(*args, **kwargs)
    ```

    Parameters:
        function: The function to apply arguments to.
        *args: Positional arguments to apply.
        **kwargs: Keyword arguments to apply.

    Returns:
        The result of applying the `function` to given arguments.
    """
    return function(*args, **kwargs)


A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")
D = TypeVar("D")
E = TypeVar("E")
F = TypeVar("F")
G = TypeVar("G")
H = TypeVar("H")


@overload
def juxt() -> DynamicCallable[EmptyTuple]: ...


@overload
def juxt(__function_a: Callable[P, A]) -> Callable[P, Tuple[A]]: ...


@overload
def juxt(
    __function_a: Callable[P, A], __function_b: Callable[P, B]
) -> Callable[P, Tuple[A, B]]: ...


@overload
def juxt(
    __function_a: Callable[P, A], __function_b: Callable[P, B], __function_c: Callable[P, C]
) -> Callable[P, Tuple[A, B, C]]: ...


@overload
def juxt(
    __function_a: Callable[P, A],
    __function_b: Callable[P, B],
    __function_c: Callable[P, C],
    __function_d: Callable[P, D],
) -> Callable[P, Tuple[A, B, C, D]]: ...


@overload
def juxt(
    __function_a: Callable[P, A],
    __function_b: Callable[P, B],
    __function_c: Callable[P, C],
    __function_d: Callable[P, D],
    __function_e: Callable[P, E],
) -> Callable[P, Tuple[A, B, C, D, E]]: ...


@overload
def juxt(
    __function_a: Callable[P, A],
    __function_b: Callable[P, B],
    __function_c: Callable[P, C],
    __function_d: Callable[P, D],
    __function_e: Callable[P, E],
    __function_f: Callable[P, F],
) -> Callable[P, Tuple[A, B, C, D, E, F]]: ...


@overload
def juxt(
    __function_a: Callable[P, A],
    __function_b: Callable[P, B],
    __function_c: Callable[P, C],
    __function_d: Callable[P, D],
    __function_e: Callable[P, E],
    __function_f: Callable[P, F],
    __function_g: Callable[P, G],
) -> Callable[P, Tuple[A, B, C, D, E, F, G]]: ...


@overload
def juxt(
    __function_a: Callable[P, A],
    __function_b: Callable[P, B],
    __function_c: Callable[P, C],
    __function_d: Callable[P, D],
    __function_e: Callable[P, E],
    __function_f: Callable[P, F],
    __function_g: Callable[P, G],
    __function_h: Callable[P, H],
) -> Callable[P, Tuple[A, B, C, D, E, F, G, H]]: ...


@overload
def juxt(
    __function_a: Callable[P, Any],
    __function_b: Callable[P, Any],
    __function_c: Callable[P, Any],
    __function_d: Callable[P, Any],
    __function_e: Callable[P, Any],
    __function_f: Callable[P, Any],
    __function_g: Callable[P, Any],
    __function_h: Callable[P, Any],
    __function_n: Callable[P, Any],
    *functions: Callable[P, Any],
) -> Callable[P, DynamicTuple[Any]]: ...


def juxt(*functions: Callable[P, Any]) -> Callable[P, DynamicTuple[Any]]:
    """Returns the function that is the juxtaposition of given functions.

    Arguments:
        *functions: Functions to return the juxtaposition for.

    Returns:
        The juxtaposition of given functions.
    """

    def call(*args: P.args, **kwargs: P.kwargs) -> DynamicTuple[Any]:
        return tuple(function(*args, **kwargs) for function in functions)

    return call
