from typing import Any

from hypothesis import given, strategies

from funcs.functions import identity


@given(strategies.from_type(type))
def test_identity(item: Any) -> None:  # type: ignore
    assert identity(item) is item
