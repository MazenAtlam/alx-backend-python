#!/usr/bin/env python3

"""A module to validate mypy"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """A zoom_array

    Args:
        lst (List): A list
        factor (int, optional): A factor. Defaults to 2.

    Returns:
        Tuple: A tuple returned
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = 12, 72, 91

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
