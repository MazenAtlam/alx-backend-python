#!/usr/bin/env python3

"""A module used to show the basics of async syntax"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """An asynchronous coroutine that waits for a random delay seconds
    and eventually returns it

    Args:
        max_delay (int, optional): The max delay in seconds. Defaults to 10.

    Returns:
        float: The delayed seconds
    """

    seconds: float = random.uniform(0, max_delay)
    await asyncio.sleep(seconds)
    return seconds
