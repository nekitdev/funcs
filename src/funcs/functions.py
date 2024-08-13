from __future__ import annotations

from typing import Awaitable, Callable, TypeVar

from typing_aliases import AnyError, AsyncCallable, Binary, GenericPredicate, Nullary
from typing_extensions import Never, ParamSpec

from funcs.decorators import wraps

__all__ = ("awaiting", "asyncify", "identity", "returns", "raises", "flip", "complement")

T = TypeVar("T")
U = TypeVar("U")

R = TypeVar("R")

P = ParamSpec("P")


async def awaiting(awaitable: Awaitable[T]) -> T:
    """Wraps an awaitable into a coroutine.

    This function is useful in, for example, [`asyncio`][asyncio],
    where some functions expect coroutines only.

    Arguments:
        awaitable: The awaitable to wrap.

    Returns:
        The result of `await awaitable`.
    """
    return await awaitable


def asyncify(function: Callable[P, R]) -> AsyncCallable[P, R]:
    """Wraps the synchronous function to be called asynchronously.

    Arguments:
        function: The synchronous function to wrap.

    Returns:
        The wrapped asynchronous function.
    """

    @wraps(function)
    async def async_function(*args: P.args, **kwargs: P.kwargs) -> R:
        return function(*args, **kwargs)

    return async_function


def identity(item: T) -> T:
    """Returns the given `item`.

    Arguments:
        item: The item to return.

    Returns:
        The given item.
    """
    return item


def returns(item: T) -> Nullary[T]:
    """Creates a function that returns the given `item` when called.

    Arguments:
        item: The item to return.

    Returns:
        The function that returns the given item.
    """

    def return_item() -> T:
        return item

    return return_item


def raises(error: AnyError) -> Nullary[Never]:
    """Creates a function that always raises the given `error` when called.

    Arguments:
        error: The error to raise.

    Returns:
        The function that always raises the given error.
    """

    def raise_error() -> Never:
        raise error

    return raise_error


def flip(binary: Binary[T, U, R]) -> Binary[U, T, R]:
    """Creates a function that flips arguments of the given `binary` function.

    Arguments:
        binary: The binary function to flip.

    Returns:
        The flipped binary function.
    """

    def flipped(u: U, t: T) -> R:
        return binary(t, u)

    return flipped


def complement(predicate: GenericPredicate[P]) -> GenericPredicate[P]:
    """Wraps the given `predicate` to return the negated result.

    Arguments:
        predicate: The predicate to wrap.

    Returns:
        The wrapped predicate.
    """

    def negate(*args: P.args, **kwargs: P.kwargs) -> bool:
        return not predicate(*args, **kwargs)

    return negate
