#!/usr/bin/env python3

"""A module has an function to be annotated"""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """A function that return a list of tuples of an iterable with its length

    Args:
        lst (Iterable[Sequence]): A list of iterables

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples
    """

    return [(i, len(i)) for i in lst]
