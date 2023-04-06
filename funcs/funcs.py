from typing import Callable, Tuple, TypeVar

from typing_extensions import Never, ParamSpec, TypeVarTuple, Unpack

from funcs.typing import (
    Binary,
    Nullary,
    Unary,
    UnpackBinary,
    UnpackNullary,
    UnpackQuaternary,
    UnpackTernary,
    UnpackUnary,
)

__all__ = (
    "always",
    "caller",
    "complement",
    "compose",
    "flip",
    "identity",
    "raises",
)

T = TypeVar("T")
U = TypeVar("U")
V = TypeVar("V")
W = TypeVar("W")

R = TypeVar("R")

P = ParamSpec("P")

Ts = TypeVarTuple("Ts")


def identity(item: T) -> T:
    return item


def always(item: T) -> Nullary[T]:
    def return_item() -> T:
        return item

    return return_item


def raises(error: AnyException) -> Nullary[Never]:
    def raise_error() -> Never:
        raise error

    return raise_error


def flip(binary: Binary[T, U, R]) -> Binary[U, T, R]:
    def flipped(u: U, t: T) -> R:
        return binary(t, u)

    return flipped


def caller(*args: P.args, **kwargs: P.kwargs) -> Unary[Callable[P, R], R]:
    def call_function(function: Callable[P, R]) -> R:
        return function(*args, **kwargs)

    return call_function


def compose_recurse(f: Unary[U, R], g: Unary[T, U]) -> Unary[T, R]:
    def composed(item: T) -> R:
        return f(g(item))

    return composed


def complement(predicate: Callable[P, bool]) -> Callable[P, bool]:
    def negate(*args: P.args, **kwargs: P.kwargs) -> bool:
        return not predicate(*args, **kwargs)

    return negate


def unpack_unary(unary: Unary[T, R]) -> UnpackUnary[T, R]:
    def unpack(items: Tuple[T]) -> R:
        (t,) = items

        return unary(t)

    return unpack


def unpack_binary(binary: Binary[T, U, R]) -> UnpackBinary[T, U, R]:
    def unpack(items: Tuple[T, U]) -> R:
        (t, u) = items

        return binary(t, u)

    return unpack
