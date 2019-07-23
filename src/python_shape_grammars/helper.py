'''Helper Functions
'''
from typing import Any


def check_argument_uniqueness(*args: Any) -> Any:
    results = [arg is not None for arg in args]
    if sum(results) != 1:
        raise ValueError(
            "Too many arguments specified. Please choose only one of " +
            f"{[type(arg) for arg in args]}")
    return args[results.index(True)]


__all__ = 'check_argument_uniqueness'
