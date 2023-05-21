from typing import Optional, TypeVar

from typing_aliases import Inspect

__all__ = ("tap", "inspect")

T = TypeVar("T")

LABEL_STRING = "{}: {}"
label_string = LABEL_STRING.format


def tap(item: T, label: Optional[str] = None) -> T:
    """Prints the given item with an optional label and returns it.

    Arguments:
        item: The item to print.
        label: The label to use.

    Returns:
        The given item.
    """
    if label is None:
        print(item)

    else:
        print(label_string(label, item))

    return item


def inspect(function: Inspect[T], item: T) -> T:
    """Inspects the given item with the `function` and returns it.

    Arguments:
        function: The function to use.
        item: The item to inspect.

    Returns:
        The given item.
    """
    function(item)

    return item
