from typing import Callable, Generic, Optional, Type, TypeVar, overload

from attrs import frozen
from typing_extensions import Literal, ParamSpec

from funcs.decorators import wraps
from funcs.types import MarkerOr, is_not_marker, marker
from funcs.typing import (
    AnyContextManager,
    AnyError,
    AnyErrorType,
    AnyErrorTypes,
    SimpleContextManager,
    Traceback,
    Unary,
    is_subclass,
)

__all__ = ("once", "reraise", "reraise_with", "suppress", "post_processing", "wrap_with")

P = ParamSpec("P")

R = TypeVar("R")
S = TypeVar("S")


def once(function: Callable[P, R]) -> Callable[P, R]:
    result: MarkerOr[R] = marker

    @wraps(function)
    def wrap(*args: P.args, **kwargs: P.kwargs) -> R:
        nonlocal result

        if is_not_marker(result):
            return result

        result = function(*args, **kwargs)

        return result

    return wrap


E = TypeVar("E", bound=AnyError)
F = TypeVar("F", bound=AnyError)


@frozen()
class Reraise(SimpleContextManager, Generic[E]):
    error: E
    error_types: AnyErrorTypes

    def __enter__(self) -> None:
        pass

    def __exit__(
        self, error_type: Optional[Type[F]], error: Optional[F], traceback: Optional[Traceback]
    ) -> None:
        if error_type is not None and error is not None:
            if is_subclass(error_type, self.error_types):
                raise self.error from error


def reraise(error: E, *error_types: AnyErrorType) -> Reraise[E]:
    return Reraise(error, error_types)


Into = Unary[AnyError, E]


@frozen()
class ReraiseWith(SimpleContextManager, Generic[E]):
    into: Into[E]
    error_types: AnyErrorTypes

    def __enter__(self) -> None:
        pass

    def __exit__(
        self, error_type: Optional[Type[F]], error: Optional[F], traceback: Optional[Traceback]
    ) -> None:
        if error_type is not None and error is not None:
            if is_subclass(error_type, self.error_types):
                raise self.into(error) from error


def reraise_with(into: Into[E], *error_types: AnyErrorType) -> ReraiseWith[E]:
    return ReraiseWith(into, error_types)


@frozen()
class Suppress:
    error_types: AnyErrorTypes

    def __enter__(self) -> None:
        pass

    @overload
    def __exit__(self, error_type: None, error: None, traceback: None) -> Literal[False]:
        ...

    @overload
    def __exit__(self, error_type: Type[E], error: E, traceback: Traceback) -> bool:
        ...

    def __exit__(
        self, error_type: Optional[Type[E]], error: Optional[E], traceback: Optional[Traceback]
    ) -> bool:
        return error_type is not None and is_subclass(error_type, self.error_types)


def suppress(*error_types: AnyErrorType) -> Suppress:
    return Suppress(error_types)


@frozen()
class PostProcessing(Generic[R, S]):
    function: Unary[R, S]

    def __call__(self, function: Callable[P, R]) -> Callable[P, S]:
        @wraps(function)
        def wrap(*args: P.args, **kwargs: P.kwargs) -> S:
            return self.function(function(*args, **kwargs))

        return wrap


def post_processing(function: Unary[R, S]) -> PostProcessing[R, S]:
    return PostProcessing(function)


@frozen()
class WrapWith:
    context_manager: AnyContextManager

    def __call__(self, function: Callable[P, R]) -> Callable[P, R]:
        @wraps(function)
        def wrap(*args: P.args, **kwargs: P.kwargs) -> R:
            with self.context_manager:
                return function(*args, **kwargs)

        return wrap


def wrap_with(context_manager: AnyContextManager) -> WrapWith:
    return WrapWith(context_manager)
