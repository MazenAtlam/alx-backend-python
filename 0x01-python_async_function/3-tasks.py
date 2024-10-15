#!/usr/bin/env python3

"""A module used to create an asynchronous task"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """A function that creates an asynchronous task

    Args:
        max_delay (int): _description_

    Returns:
        asyncio.Task: _description_
    """

    return asyncio.create_task(wait_random(max_delay))
