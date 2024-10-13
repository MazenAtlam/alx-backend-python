#!/usr/bin/env python3

"""A module has a sum_mixed_list function that
returns the sum of a list of numbers
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """A type-annotated function that calculates the sum of a list of numbers

    Args:
        mxd_lst (List[float, int]): A list of numbers

    Returns:
        float: The sum of the numbers
    """

    return sum(mxd_lst)
