#!/usr/bin/env python3

"""A module has a to_kv function that returns a tuple of k and square of v"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """A type-annotated function that returns a tuple of k and square of v

    Args:
        k (str): A string that is the first element of the tuple returned
        v (Union[int, float]): A number that its square is the second element

    Returns:
        Tuple[str, float]: A tuple of k and square of v
    """

    return tuple(k, float(v * v))
