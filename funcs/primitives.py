__all__ = ("increment", "decrement", "is_even", "is_odd")


def increment(x: int) -> int:
    return x + 1


def decrement(x: int) -> int:
    return x - 1


def is_even(x: int) -> bool:
    return not x % 2


def is_odd(x: int) -> bool:
    return not is_even(x)
