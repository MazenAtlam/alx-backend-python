#!/usr/bin/env python3

"""A module has an function to be annotated"""

from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
    -> Union[Any, T]:
    """A function that gets the first element of a dictionary

    Args:
        dct (Mapping): A dictionary of keys and values
        key (Any): The key of the element
        default: The default key

    Returns:
        Union[T, None]: The first element or None if it is empty
    """

    if key in dct:
        return dct[key]
    else:
        return default
