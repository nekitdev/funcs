from typing import Any, TypeVar, overload

from typing_aliases import Unary

from funcs.reduction import fold

__all__ = ("compose", "compose_once", "pipe", "pipe_once")

T = TypeVar("T")
U = TypeVar("U")

R = TypeVar("R")

A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")
D = TypeVar("D")
E = TypeVar("E")
F = TypeVar("F")
G = TypeVar("G")
H = TypeVar("H")


def pipe_once(inner: Unary[T, U], outer: Unary[U, R]) -> Unary[T, R]:
    """Composes two functions from left to right into one function.

    For instance, `pipe_once(f, g)(x)` is equivalent to `g(f(x))`.

    Arguments:
        inner: The inner function.
        outer: The outer function.

    Returns:
        The composed function.
    """

    def piped(item: T) -> R:
        return outer(inner(item))

    return piped


@overload
def pipe(__function_a: Unary[A, R]) -> Unary[A, R]:
    ...


@overload
def pipe(__function_a: Unary[A, B], __function_b: Unary[B, R]) -> Unary[A, R]:
    ...


@overload
def pipe(
    __function_a: Unary[A, B], __function_b: Unary[B, C], __function_c: Unary[C, R]
) -> Unary[A, R]:
    ...


@overload
def pipe(
    __function_a: Unary[A, B],
    __function_b: Unary[B, C],
    __function_c: Unary[C, D],
    __function_d: Unary[D, R],
) -> Unary[A, R]:
    ...


@overload
def pipe(
    __function_a: Unary[A, B],
    __function_b: Unary[B, C],
    __function_c: Unary[C, D],
    __function_d: Unary[D, E],
    __function_e: Unary[E, R],
) -> Unary[A, R]:
    ...


@overload
def pipe(
    __function_a: Unary[A, B],
    __function_b: Unary[B, C],
    __function_c: Unary[C, D],
    __function_d: Unary[D, E],
    __function_e: Unary[E, F],
    __function_f: Unary[F, R],
) -> Unary[A, R]:
    ...


@overload
def pipe(
    __function_a: Unary[A, B],
    __function_b: Unary[B, C],
    __function_c: Unary[C, D],
    __function_d: Unary[D, E],
    __function_e: Unary[E, F],
    __function_f: Unary[F, G],
    __function_g: Unary[G, R],
) -> Unary[A, R]:
    ...


@overload
def pipe(
    __function_a: Unary[A, B],
    __function_b: Unary[B, C],
    __function_c: Unary[C, D],
    __function_d: Unary[D, E],
    __function_e: Unary[E, F],
    __function_f: Unary[F, G],
    __function_g: Unary[G, H],
    __function_h: Unary[H, R],
) -> Unary[A, R]:
    ...


@overload
def pipe(innermost: Unary[T, Any], *functions: Unary[Any, Any]) -> Unary[T, Any]:
    ...


def pipe(innermost: Unary[T, Any], *functions: Unary[Any, Any]) -> Unary[T, Any]:
    """Composes multiple functions from left to right into one function.

    For instance, `pipe(f, g)(x)` is equivalent to `g(f(x))`.

    This function is equivalent to:

    ```python
    fold(innermost, pipe_once, functions)
    ```

    Arguments:
        innermost: The innermost function.
        *functions: The rest of the functions.

    Returns:
        The composed function.
    """
    return fold(innermost, pipe_once, functions)


def compose_once(outer: Unary[U, R], inner: Unary[T, U]) -> Unary[T, R]:
    """Composes two functions from right to left into one function.

    For instance, `compose_once(f, g)(x)` is equivalent to `f(g(x))`.

    Arguments:
        outer: The outer function.
        inner: The inner function.

    Returns:
        The composed function.
    """

    def composed(item: T) -> R:
        return outer(inner(item))

    return composed


@overload
def compose(__function_a: Unary[A, R]) -> Unary[A, R]:
    ...


@overload
def compose(__function_b: Unary[B, R], __function_a: Unary[A, B]) -> Unary[A, R]:
    ...


@overload
def compose(
    __function_c: Unary[C, R], __function_b: Unary[B, C], __function_a: Unary[A, B]
) -> Unary[A, R]:
    ...


@overload
def compose(
    __function_d: Unary[D, R],
    __function_c: Unary[C, D],
    __function_b: Unary[B, C],
    __function_a: Unary[A, B],
) -> Unary[A, R]:
    ...


@overload
def compose(
    __function_e: Unary[E, R],
    __function_d: Unary[D, E],
    __function_c: Unary[C, D],
    __function_b: Unary[B, C],
    __function_a: Unary[A, B],
) -> Unary[A, R]:
    ...


@overload
def compose(
    __function_f: Unary[F, R],
    __function_e: Unary[E, F],
    __function_d: Unary[D, E],
    __function_c: Unary[C, D],
    __function_b: Unary[B, C],
    __function_a: Unary[A, B],
) -> Unary[A, R]:
    ...


@overload
def compose(
    __function_g: Unary[G, R],
    __function_f: Unary[F, G],
    __function_e: Unary[E, F],
    __function_d: Unary[D, E],
    __function_c: Unary[C, D],
    __function_b: Unary[B, C],
    __function_a: Unary[A, B],
) -> Unary[A, R]:
    ...


@overload
def compose(
    __function_h: Unary[H, R],
    __function_g: Unary[G, H],
    __function_f: Unary[F, G],
    __function_e: Unary[E, F],
    __function_d: Unary[D, E],
    __function_c: Unary[C, D],
    __function_b: Unary[B, C],
    __function_a: Unary[A, B],
) -> Unary[A, R]:
    ...


@overload
def compose(outermost: Unary[Any, T], *functions: Unary[Any, Any]) -> Unary[Any, T]:
    ...


def compose(outermost: Unary[Any, T], *functions: Unary[Any, Any]) -> Unary[Any, T]:
    """Composes multiple functions from right to left into one.

    For instance, `compose(f, g)(x)` is equivalent to `f(g(x))`.

    This function is equivalent to:

    ```python
    fold(outermost, compose_once, functions)
    ```

    Arguments:
        outermost: The outermost function.
        *functions: The rest of the functions.

    Returns:
        The composed function.
    """
    return fold(outermost, compose_once, functions)
