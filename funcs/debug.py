from typing import Optional, TypeVar

__all__ = ("tap",)

T = TypeVar("T")

LABEL_STRING = "{}: {}"
label_string = LABEL_STRING.format


def tap(item: T, label: Optional[str] = None) -> T:
    if label is None:
        print(item)

    else:
        print(label_string(label, item))

    return item
