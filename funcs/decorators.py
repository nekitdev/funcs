from functools import lru_cache
from functools import wraps as standard_wraps

__all__ = ("wraps", "cache", "cache_typed")

wraps = standard_wraps
"""An alias of the standard `wraps` function that implements wrapping."""

cache = lru_cache(None)
"""An alias of the standard `lru_cache` function with unbounded cache."""

cache_typed = lru_cache(None, typed=True)
"""A variantion of [`cache`][funcs.decorators.cache] that uses types."""
