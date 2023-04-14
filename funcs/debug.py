from typing import Optional, TypeVar

from funcs.typing import Inspect

__all__ = ("tap", "inspect")

T = TypeVar("T")

LABEL_STRING = "{}: {}"
label_string = LABEL_STRING.format


def tap(item: T, label: Optional[str] = None) -> T:
    if label is None:
        print(item)

    else:
        print(label_string(label, item))

    return item


def inspect(function: Inspect[T], item: T) -> T:
    function(item)

    return item
