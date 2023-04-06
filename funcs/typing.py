from typing import Awaitable, Callable, Tuple, TypeVar

from typing_extensions import TypeAlias, TypeVarTuple

__all__ = (
    "AnyException",
    "EmptyTuple",
    "Nullary",
    "Unary",
    "Binary",
    "Ternary",
    "Quaternary",
    "Variable",
    "UnpackNullary",
    "UnpackUnary",
    "UnpackBinary",
    "UnpackTernary",
    "UnpackQuaternary",
    "UnpackVariable",
    "AsyncNullary",
    "AsyncUnary",
    "AsyncBinary",
    "AsyncTernary",
    "AsyncQuaternary",
    "AsyncVariable",
)

AnyException: TypeAlias = BaseException

EmptyTuple = Tuple[()]

T = TypeVar("T")
U = TypeVar("U")
V = TypeVar("V")
W = TypeVar("W")

Ts = TypeVarTuple("Ts")
R = TypeVar("R")

Nullary = Callable[[], R]
Unary = Callable[[T], R]
Binary = Callable[[T, U], R]
Ternary = Callable[[T, U, V], R]
Quaternary = Callable[[T, U, V, W], R]

Variable = Callable[[Unpack[Ts]], R]

UnpackNullary = Unary[EmptyTuple, R]
UnpackUnary = Unary[Tuple[T], R]
UnpackBinary = Unary[Tuple[T, U], R]
UnpackTernary = Unary[Tuple[T, U, V], R]
UnpackQuaternary = Unary[Tuple[T, U, V, W], R]

UnpackVariable = Unary[Tuple[Unpack[Ts]], R]

AsyncNullary = Nullary[Awaitable[R]]
AsyncUnary = Unary[T, Awaitable[R]]
AsyncBinary = Binary[T, U, Awaitable[R]]
AsyncTernary = Ternary[T, U, V, Awaitable[R]]
AsyncQuaternary = Quaternary[T, U, V, W, Awaitable[R]]

AsyncVariable = Variable[Ts, Awaitable[R]]
