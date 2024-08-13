from __future__ import annotations

from typing import Any

from funcs.functions import identity
from hypothesis import given, strategies


@given(strategies.from_type(type))
def test_identity(item: Any) -> None:
    assert identity(item) is item
