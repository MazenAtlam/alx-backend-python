#!/usr/bin/env python3

"""A module used to measure the total execution time"""

import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """A function that measures the total execution time for wait_n

    Args:
        n (int): The number of times wait_random should be called
        max_delay (int): The maximum delay of wait_random

    Returns:
        float: The total execution time
    """

    t0: float = time.time()
    await wait_n(n, max_delay)
    t1: float = time.time()

    total_time: float = t1 - t0

    return total_time / n
