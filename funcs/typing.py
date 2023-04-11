from builtins import isinstance as is_instance
from builtins import issubclass as is_subclass
from types import TracebackType as Traceback
from typing import Any, Awaitable, Callable, ContextManager, Optional, Tuple, Type, TypeVar

from typing_extensions import ParamSpec, TypeAlias, TypeGuard

__all__ = (
    "Traceback",
    "AnyError",
    "AnyErrorType",
    "Error",
    "ErrorType",
    "AnyContextManager",
    "SimpleContextManager",
    "EmptyTuple",
    "DynamicTuple",
    "AnyTuple",
    "AnyErrorTypes",
    "ErrorTypes",
    "DynamicCallable",
    "AnyCallable",
    "Nullary",
    "Unary",
    "Binary",
    "Ternary",
    "Quaternary",
    "Predicate",
    "GenericPredicate",
    "UnpackNullary",
    "UnpackUnary",
    "UnpackBinary",
    "UnpackTernary",
    "UnpackQuaternary",
    "AsyncNullary",
    "AsyncUnary",
    "AsyncBinary",
    "AsyncTernary",
    "AsyncQuaternary",
    "AsyncPredicate",
    "AsyncGenericPredicate",
    "is_instance",
    "is_subclass",
    "is_none",
    "is_not_none",
)

AnyError: TypeAlias = BaseException
AnyErrorType = Type[AnyError]

Error: TypeAlias = Exception
ErrorType = Type[Error]

AnyContextManager = ContextManager[Any]
SimpleContextManager = ContextManager[None]

EmptyTuple = Tuple[()]

T = TypeVar("T")
U = TypeVar("U")
V = TypeVar("V")
W = TypeVar("W")

R = TypeVar("R")

P = ParamSpec("P")

DynamicTuple = Tuple[T, ...]
AnyTuple = DynamicTuple[Any]

AnyErrorTypes = DynamicTuple[AnyErrorType]
ErrorTypes = DynamicTuple[ErrorType]

DynamicCallable = Callable[..., R]
AnyCallable = DynamicCallable[Any]

F = TypeVar("F", bound=AnyCallable)
G = TypeVar("G", bound=AnyCallable)

Nullary = Callable[[], R]
Unary = Callable[[T], R]
Binary = Callable[[T, U], R]
Ternary = Callable[[T, U, V], R]
Quaternary = Callable[[T, U, V, W], R]

Predicate = Unary[T, bool]

Decorator = Unary[F, G]
DecoratorIdentity = Decorator[F, F]

GenericPredicate = Callable[P, bool]

UnpackNullary = Unary[EmptyTuple, R]
UnpackUnary = Unary[Tuple[T], R]
UnpackBinary = Unary[Tuple[T, U], R]
UnpackTernary = Unary[Tuple[T, U, V], R]
UnpackQuaternary = Unary[Tuple[T, U, V, W], R]

AsyncCallable = Callable[P, Awaitable[R]]

AsyncNullary = Nullary[Awaitable[R]]
AsyncUnary = Unary[T, Awaitable[R]]
AsyncBinary = Binary[T, U, Awaitable[R]]
AsyncTernary = Ternary[T, U, V, Awaitable[R]]
AsyncQuaternary = Quaternary[T, U, V, W, Awaitable[R]]

AsyncPredicate = AsyncUnary[T, bool]

AsyncGenericPredicate = AsyncCallable[P, bool]


def is_none(item: Optional[Any]) -> TypeGuard[None]:
    return item is None


def is_not_none(item: Optional[T]) -> TypeGuard[T]:
    return item is not None
