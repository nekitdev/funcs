"""Functional programming in Python."""

from __future__ import annotations

__description__ = "Functional programming in Python."
__url__ = "https://github.com/nekitdev/funcs"

__title__ = "funcs"
__author__ = "nekitdev"
__license__ = "MIT"
__version__ = "0.11.0"

from funcs.application import apply, juxt, partial
from funcs.callers import caller, method_caller
from funcs.composition import compose, compose_once, pipe, pipe_once
from funcs.debugging import inspect, tap
from funcs.decorators import cache, cache_typed, lru_cache, wraps
from funcs.flows import once, post_processing, reraise, reraise_with, suppress, wrap_with
from funcs.functions import asyncify, awaiting, complement, flip, identity, raises, returns
from funcs.getters import attribute_getter, item_getter
from funcs.primitives import decrement, increment, is_even, is_odd
from funcs.reduction import fold, reduce
from funcs.unpacking import (
    unpack_binary,
    unpack_nullary,
    unpack_quaternary,
    unpack_ternary,
    unpack_unary,
)

__all__ = (
    # application
    "apply",
    "partial",
    "juxt",
    # callers
    "caller",
    "method_caller",
    # composition
    "compose",
    "compose_once",
    "pipe",
    "pipe_once",
    # debugging
    "inspect",
    "tap",
    # decorators
    "wraps",
    "lru_cache",
    "cache",
    "cache_typed",
    # flows
    "once",
    "reraise",
    "reraise_with",
    "suppress",
    "post_processing",
    "wrap_with",
    # functions
    "awaiting",
    "asyncify",
    "identity",
    "returns",
    "raises",
    "flip",
    "complement",
    # getters
    "attribute_getter",
    "item_getter",
    # primitives
    "decrement",
    "increment",
    "is_even",
    "is_odd",
    # reduction
    "reduce",
    "fold",
    # unpacking
    "unpack_nullary",
    "unpack_unary",
    "unpack_binary",
    "unpack_ternary",
    "unpack_quaternary",
)
