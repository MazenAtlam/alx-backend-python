#!/usr/bin/env python3

"""A module has an function to be annotated"""

from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """A function that gets the first element of a sequence

    Args:
        lst (Sequence[Any]): A sequence of elements

    Returns:
        Union[Any, None]: The first element or None if it is empty
    """

    if lst:
        return lst[0]
    else:
        return None
