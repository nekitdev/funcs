from typing import TypeVar

from typing_extensions import Never, ParamSpec

from funcs.typing import AnyError, Binary, GenericPredicate, Nullary

__all__ = ("identity", "always", "raises", "flip", "complement")

T = TypeVar("T")
U = TypeVar("U")

R = TypeVar("R")

P = ParamSpec("P")


def identity(item: T) -> T:
    return item


def always(item: T) -> Nullary[T]:
    def return_item() -> T:
        return item

    return return_item


def raises(error: AnyError) -> Nullary[Never]:
    def raise_error() -> Never:
        raise error

    return raise_error


def flip(binary: Binary[T, U, R]) -> Binary[U, T, R]:
    def flipped(u: U, t: T) -> R:
        return binary(t, u)

    return flipped


def complement(predicate: GenericPredicate[P]) -> GenericPredicate[P]:
    def negate(*args: P.args, **kwargs: P.kwargs) -> bool:
        return not predicate(*args, **kwargs)

    return negate
