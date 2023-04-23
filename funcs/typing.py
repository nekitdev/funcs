from builtins import isinstance as is_instance
from builtins import issubclass as is_subclass
from types import TracebackType as Traceback
from typing import Any, Awaitable, Callable, ContextManager, Optional, Tuple, Type, TypeVar

from typing_extensions import ParamSpec, TypeAlias, TypeGuard

__all__ = (
    "Traceback",
    "AnyError",
    "AnyErrorType",
    "NormalError",
    "NormalErrorType",
    "AnyContextManager",
    "SimpleContextManager",
    "EmptyTuple",
    "Tuple1",
    "Tuple2",
    "Tuple3",
    "Tuple4",
    "Tuple5",
    "Tuple6",
    "Tuple7",
    "Tuple8",
    "DynamicTuple",
    "AnyTuple",
    "AnyErrorTypes",
    "NormalErrorTypes",
    "DynamicCallable",
    "AnyCallable",
    "Nullary",
    "Unary",
    "Binary",
    "Ternary",
    "Quaternary",
    "Identity",
    "Inspect",
    "Predicate",
    "Decorator",
    "DecoratorIdentity",
    "GenericPredicate",
    "Compare",
    "UnpackNullary",
    "UnpackUnary",
    "UnpackBinary",
    "UnpackTernary",
    "UnpackQuaternary",
    "AsyncCallable",
    "DynamicAsyncCallable",
    "AnyAsyncCallable",
    "AsyncNullary",
    "AsyncUnary",
    "AsyncBinary",
    "AsyncTernary",
    "AsyncQuaternary",
    "AsyncIdentity",
    "AsyncInspect",
    "AsyncPredicate",
    "AsyncGenericPredicate",
    "AsyncCompare",
    "is_instance",
    "is_subclass",
    "is_none",
    "is_not_none",
)

AnyError: TypeAlias = BaseException
"""Represents any errors."""
AnyErrorType = Type[AnyError]
"""Represents any error types."""

NormalError: TypeAlias = Exception
"""Represents normal errors."""
NormalErrorType = Type[NormalError]
"""Represents normal error types."""

AnyContextManager = ContextManager[Any]
"""Represents any context managers."""
SimpleContextManager = ContextManager[None]
"""Represents simple context managers that don't return anything on enter."""

EmptyTuple = Tuple[()]
"""Represents empty tuples `()`."""

T = TypeVar("T")
U = TypeVar("U")
V = TypeVar("V")
W = TypeVar("W")

R = TypeVar("R")

P = ParamSpec("P")

Tuple1 = Tuple[T]
"""Represents homogeneous 1-tuples `(T)`."""
Tuple2 = Tuple[T, T]
"""Represents homogeneous 2-tuples `(T, T)`."""
Tuple3 = Tuple[T, T, T]
"""Represents homogeneous 3-tuples `(T, T, T)`."""
Tuple4 = Tuple[T, T, T, T]
"""Represents homogeneous 4-tuples `(T, T, T, T)`."""
Tuple5 = Tuple[T, T, T, T, T]
"""Represents homogeneous 5-tuples `(T, T, T, T, T)`."""
Tuple6 = Tuple[T, T, T, T, T, T]
"""Represents homogeneous 6-tuples `(T, T, T, T, T, T)`."""
Tuple7 = Tuple[T, T, T, T, T, T, T]
"""Represents homogeneous 7-tuples `(T, T, T, T, T, T, T)`."""
Tuple8 = Tuple[T, T, T, T, T, T, T, T]
"""Represents homogeneous 8-tuples `(T, T, T, T, T, T, T, T)`."""

DynamicTuple = Tuple[T, ...]
"""Represents homogeneous tuples of any length `(T, ...)`."""
AnyTuple = DynamicTuple[Any]
"""Represents any tuples `(Any, ...)`."""

AnyErrorTypes = DynamicTuple[AnyErrorType]
"""Represents tuples of any error types `(AnyErrorType, ...)`."""
NormalErrorTypes = DynamicTuple[NormalErrorType]
"""Represents tuples of normal error types `(NormalErrorType, ...)`."""

DynamicCallable = Callable[..., R]
"""Represents dynamic callables `(...) -> R`."""
AnyCallable = DynamicCallable[Any]
"""Represents any callables `(...) -> Any`."""

F = TypeVar("F", bound=AnyCallable)
G = TypeVar("G", bound=AnyCallable)

Nullary = Callable[[], R]
"""Represents nullary functions `() -> R`."""
Unary = Callable[[T], R]
"""Represents unary functions `(T) -> R`."""
Binary = Callable[[T, U], R]
"""Represents binary functions `(T, U) -> R`."""
Ternary = Callable[[T, U, V], R]
"""Represents ternary functions `(T, U, V) -> R`."""
Quaternary = Callable[[T, U, V, W], R]
"""Represents quaternary functions `(T, U, V, W) -> R`."""

Identity = Unary[T, T]
"""Represents identity functions `(T) -> T`."""

Inspect = Unary[T, None]
"""Represents inspect functions `(T)`."""

Predicate = Unary[T, bool]
"""Represents predicates `(T) -> bool`."""

Decorator = Unary[F, G]
"""Represents decorators `(F) -> G`."""
DecoratorIdentity = Identity[F]
"""Represents identity decorators `(F) -> F`."""

GenericPredicate = Callable[P, bool]
"""Represents generic predicates `(P) -> bool`."""

Compare = Binary[T, U, bool]
"""Represents comparison functions `(T, U) -> bool`."""

UnpackNullary = Unary[EmptyTuple, R]
"""Represents unpacking nullary functions `(()) -> R`."""
UnpackUnary = Unary[Tuple[T], R]
"""Represents unpacking unary functions `((T)) -> R`."""
UnpackBinary = Unary[Tuple[T, U], R]
"""Represents unpacking binary functions `((T, U)) -> R`."""
UnpackTernary = Unary[Tuple[T, U, V], R]
"""Represents unpacking ternary functions `((T, U, V)) -> R`."""
UnpackQuaternary = Unary[Tuple[T, U, V, W], R]
"""Represents unpacking quaternary functions `((T, U, V, W)) -> R`."""

AsyncCallable = Callable[P, Awaitable[R]]
"""Represents async callables `async (P) -> R`."""
DynamicAsyncCallable = AsyncCallable[..., R]  # type: ignore
"""Represents dynamic async callables `async (...) -> R`."""
AnyAsyncCallable = DynamicAsyncCallable[Any]
"""Represents any async callables `async (...) -> Any`."""

AsyncNullary = Nullary[Awaitable[R]]
"""Represents async nullary functions `async () -> R`."""
AsyncUnary = Unary[T, Awaitable[R]]
"""Represents async unary functions `async (T) -> R`."""
AsyncBinary = Binary[T, U, Awaitable[R]]
"""Represents async binary functions `async (T, U) -> R`."""
AsyncTernary = Ternary[T, U, V, Awaitable[R]]
"""Represents async ternary functions `async (T, U, V) -> R`."""
AsyncQuaternary = Quaternary[T, U, V, W, Awaitable[R]]
"""Represents async quaternary functions `async (T, U, V, W) -> R`."""

AsyncIdentity = AsyncUnary[T, T]
"""Represents async identity functions `async (T) -> T`."""

AsyncInspect = AsyncUnary[T, None]
"""Represents async inspect functions `async (T)`."""

AsyncPredicate = AsyncUnary[T, bool]
"""Represents async predicates `async (T) -> bool`."""

AsyncGenericPredicate = AsyncCallable[P, bool]
"""Represents async generic predicates `async (P) -> bool`."""

AsyncCompare = AsyncBinary[T, U, bool]
"""Represents async comparison functions `async (T, U) -> bool`."""


def is_none(item: Optional[Any]) -> TypeGuard[None]:
    """Checks if the given `item` is [`None`][None].

    Arguments:
        item: The item to check.

    Returns:
        Whether the given item is [`None`][None].
    """
    return item is None


def is_not_none(item: Optional[T]) -> TypeGuard[T]:
    """Checks if the given `item` is *not* [`None`][None].

    Arguments:
        item: The item to check.

    Returns:
        Whether the given item is *not* [`None`][None].
    """
    return item is not None
