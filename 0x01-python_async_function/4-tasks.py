#!/usr/bin/env python3

"""A module used to show the concurrent coroutines"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """An asynchronous coroutine that spawns wait_random n times

    Args:
        n (int): The number of times wait_random should be called
        max_delay (int): The maximum delay of wait_random

    Returns:
        List[float]: The list of the delays should be in ascending order
    """

    delays: List[float] = await asyncio.gather(
        *tuple(task_wait_random(max_delay) for _ in range(n))
    )

    return sorted(delays)

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
