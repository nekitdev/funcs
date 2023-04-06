from typing import Callable, Tuple, TypeVar

from typing_extensions import Never, ParamSpec, TypeVarTuple, Unpack

from funcs.typing import (
    Binary,
    Nullary,
    Quaternary,
    Ternary,
    Unary,
    UnpackBinary,
    UnpackNullary,
    UnpackQuaternary,
    UnpackTernary,
    UnpackUnary,
    UnpackVariable,
    Variable,
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


def unpack_nullary(function: Nullary[R]) -> UnpackNullary[R]:
    def unpack(items: EmptyTuple) -> R:
        return function()

    return unpack


def unpack_unary(function: Unary[T, R]) -> UnpackUnary[T, R]:
    def unpack(items: Tuple[T]) -> R:
        (t,) = items

        return function(t)

    return unpack


def unpack_binary(function: Binary[T, U, R]) -> UnpackBinary[T, U, R]:
    def unpack(items: Tuple[T, U]) -> R:
        (t, u) = items

        return function(t, u)

    return unpack


def unpack_ternary(function: Ternary[T, U, V, R]) -> UnpackTernary[T, U, V, R]:
    def unpack(items: Tuple[T, U, V]) -> R:
        (t, u, v) = items

        return function(t, u, v)

    return unpack


def unpack_quaternary(function: Quaternary[T, U, V, W, R]) -> UnpackQuaternary[T, U, V, W, R]:
    def unpack(items: Tuple[T, U, V, W]) -> R:
        (t, u, v, w) = items

        return function(t, u, v, w)

    return unpack


def unpack_variable(function: Variable[Ts, R]) -> UnpackVariable[Ts, R]:
    def unpack(items: Tuple[Unpack[Ts]]) -> R:
        return function(*items)

    return unpack
