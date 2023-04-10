from functools import partial as standard_partial
from typing import Callable, TypeVar

from typing_extensions import ParamSpec

__all__ = ("apply", "partial")

P = ParamSpec("P")
R = TypeVar("R")

partial = standard_partial
"""An alias of the standard `partial` type that implements partial application."""


def apply(function: Callable[P, R], *args: P.args, **kwargs: P.kwargs) -> R:
    """Applies the `function` to given positional and keyword arguments.

    ```python
    apply(function, *args, **kwargs)
    ```

    Is identical to:

    ```python
    function(*args, **kwargs)
    ```

    Parameters:
        function: The function to apply arguments to.
        *args: Positional arguments to apply.
        **kwargs: Keyword arguments to apply.

    Returns:
        The result of applying the `function` to given arguments.
    """
    return function(*args, **kwargs)
