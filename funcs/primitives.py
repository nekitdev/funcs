__all__ = ("increment", "decrement", "is_even", "is_odd")


def increment(x: int) -> int:
    """Increments `x` by 1.

    Arguments:
        x: The value to increment.

    Returns:
        The incremented value.
    """
    return x + 1


def decrement(x: int) -> int:
    """Decrements `x` by 1.

    Arguments:
        x: The value to decrement.

    Returns:
        The decremented value.
    """
    return x - 1


def is_even(x: int) -> bool:
    """Checks if `x` is even.

    Arguments:
        x: The value to check.

    Returns:
        Whether `x` is even.
    """
    return not x % 2


def is_odd(x: int) -> bool:
    """Checks if `x` is odd.

    Arguments:
        x: The value to check.

    Returns:
        Whether `x` is odd.
    """
    return not is_even(x)
