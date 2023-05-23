from types import TracebackType as Traceback
from typing import Callable, Generic, Optional, Type, TypeVar, overload

from attrs import frozen
from typing_aliases import (
    AnyContextManager,
    AnyError,
    AnyErrorType,
    AnyErrorTypes,
    SimpleContextManager,
    Unary,
    is_subclass,
)
from typing_extensions import Literal, ParamSpec, final

from funcs.decorators import wraps
from funcs.types import MarkerOr, is_not_marker, marker

__all__ = ("once", "reraise", "reraise_with", "suppress", "post_processing", "wrap_with")

P = ParamSpec("P")

R = TypeVar("R")
S = TypeVar("S")


def once(function: Callable[P, R]) -> Callable[P, R]:
    """Wraps the function to be called once, and then the
    computed result is returned on subsequent calls.

    Arguments:
        function: The function to wrap.

    Returns:
        The wrapped function.
    """
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


@final
@frozen()
class Reraise(SimpleContextManager, Generic[E]):
    """Represents context managers that reraise errors of given `error_types` as `error`."""

    error: E
    """The error to raise."""
    error_types: AnyErrorTypes
    """The error types to reraise."""

    def __enter__(self) -> None:
        pass

    def __exit__(
        self, error_type: Optional[Type[F]], error: Optional[F], traceback: Optional[Traceback]
    ) -> None:
        if error_type is not None and error is not None:
            if is_subclass(error_type, self.error_types):
                raise self.error from error


def reraise(error: E, *error_types: AnyErrorType) -> Reraise[E]:
    """Constructs the [`Reraise[E]`][funcs.flow.Reraise] context manager
    that reraises errors of given `error_types` as `error`.

    Arguments:
        error: The error to raise.
        *error_types: The error types to reraise.

    Returns:
        The constructed [`Reraise[E]`][funcs.flow.Reraise] context manager.
    """
    return Reraise(error, error_types)


Into = Unary[AnyError, E]


@final
@frozen()
class ReraiseWith(SimpleContextManager, Generic[E]):
    """Represents context managers that reraise errors of given `error_types` as `error`,
    which is computed dynamically from the original error.
    """

    into: Into[E]
    """The function that computes the error to raise from the original error."""
    error_types: AnyErrorTypes
    """The error types to reraise."""

    def __enter__(self) -> None:
        pass

    def __exit__(
        self, error_type: Optional[Type[F]], error: Optional[F], traceback: Optional[Traceback]
    ) -> None:
        if error_type is not None and error is not None:
            if is_subclass(error_type, self.error_types):
                raise self.into(error) from error


def reraise_with(into: Into[E], *error_types: AnyErrorType) -> ReraiseWith[E]:
    """Constructs the [`ReraiseWith[E]`][funcs.flow.ReraiseWith] context manager
    that reraises errors of given `error_types` as `error`, which is computed dynamically
    from the original error.

    Arguments:
        into: The function that computes the error to raise from the original error.
        *error_types: The error types to reraise.

    Returns:
        The constructed [`ReraiseWith[E]`][funcs.flow.ReraiseWith] context manager.
    """
    return ReraiseWith(into, error_types)


@final
@frozen()
class Suppress:
    """Represents context managers that suppress errors of given `error_types`."""

    error_types: AnyErrorTypes
    """The error types to suppress."""

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
    """Constructs the [`Suppress`][funcs.flow.Suppress] context manager used to suppress
    errors of given `error_types`.

    Arguments:
        *error_types: The error types to suppress.

    Returns:
        The constructed [`Suppress`][funcs.flow.Suppress] context manager.
    """
    return Suppress(error_types)


@final
@frozen()
class PostProcessing(Generic[R, S]):
    """Represents decorators that post-process results of function calls."""

    function: Unary[R, S]

    def __call__(self, function: Callable[P, R]) -> Callable[P, S]:
        @wraps(function)
        def wrap(*args: P.args, **kwargs: P.kwargs) -> S:
            return self.function(function(*args, **kwargs))

        return wrap


def post_processing(function: Unary[R, S]) -> PostProcessing[R, S]:
    """Constructs the [`PostProcessing[R, S]`][funcs.flow.PostProcessing] decorator
    which post-processes results of function calls.

    Arguments:
        function: The post-processing function.

    Returns:
        The constructed [`PostProcessing[R, S]`][funcs.flow.PostProcessing] decorator.
    """
    return PostProcessing(function)


@frozen()
class WrapWith:
    """Represents decorators that wrap function calls with the given `context_manager`."""

    context_manager: AnyContextManager
    """The context manager to wrap function calls with."""

    def __call__(self, function: Callable[P, R]) -> Callable[P, R]:
        @wraps(function)
        def wrap(*args: P.args, **kwargs: P.kwargs) -> R:
            with self.context_manager:
                return function(*args, **kwargs)

        return wrap


def wrap_with(context_manager: AnyContextManager) -> WrapWith:
    """Constructs the [`WrapWith`][funcs.flow.WrapWith] decorator that wraps function calls
    with the given `context_manager`.

    Arguments:
        context_manager: The context manager to wrap function calls with.

    Returns:
        The constructed [`WrapWith`][funcs.flow.WrapWith] decorator.
    """
    return WrapWith(context_manager)
