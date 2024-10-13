#!/usr/bin/env python3

"""A module has a make_multiplier function that
returns a function that multiplies a float by multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A type-annotated function that makes a function
    that multiplies a float by multiplier

    Args:
        multiplier (float): The number which is multiplied by

    Returns:
        Callable[[float], float]: A function that multiplies a float
        by multiplier
    """

    def fun(num: float) -> float:
        return num * multiplier

    return fun
