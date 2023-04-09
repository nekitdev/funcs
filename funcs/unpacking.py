from typing import Tuple, TypeVar

from funcs.typing import (
    Binary,
    EmptyTuple,
    Nullary,
    Quaternary,
    Ternary,
    Unary,
    UnpackBinary,
    UnpackNullary,
    UnpackQuaternary,
    UnpackTernary,
    UnpackUnary,
)

__all__ = ("unpack_nullary", "unpack_unary", "unpack_binary", "unpack_ternary", "unpack_quaternary")

T = TypeVar("T")
U = TypeVar("U")
V = TypeVar("V")
W = TypeVar("W")

R = TypeVar("R")


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
