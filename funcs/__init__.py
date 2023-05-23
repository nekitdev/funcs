"""Functional programming in Python."""

__description__ = "Functional programming in Python."
__url__ = "https://github.com/nekitdev/funcs"

__title__ = "funcs"
__author__ = "nekitdev"
__license__ = "MIT"
__version__ = "0.7.1"

from funcs.application import apply, partial
from funcs.callers import caller, method_caller
from funcs.composition import compose, compose_once, pipe, pipe_once
from funcs.debug import inspect, tap
from funcs.decorators import wraps
from funcs.flow import once, post_processing, reraise, reraise_with, suppress, wrap_with
from funcs.functions import always, asyncify, complement, flip, identity, raises
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
    # callers
    "caller",
    "method_caller",
    # composition
    "compose",
    "compose_once",
    "pipe",
    "pipe_once",
    # debug
    "inspect",
    "tap",
    # decorators
    "wraps",
    # flow
    "once",
    "reraise",
    "reraise_with",
    "suppress",
    "post_processing",
    "wrap_with",
    # functions
    "asyncify",
    "identity",
    "always",
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
