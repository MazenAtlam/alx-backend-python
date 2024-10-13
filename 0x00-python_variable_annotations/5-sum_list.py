#!/usr/bin/env python3

"""A module has a sum_list function that returns the sum of a list of floats"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """A type-annotated function that calculates the sum of a list of floats

    Args:
        input_list (List[float]): A list of float numbers

    Returns:
        float: The sum of the float numbers
    """

    return sum(input_list)
