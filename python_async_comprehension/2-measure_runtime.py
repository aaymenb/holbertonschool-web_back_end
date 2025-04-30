#!/usr/bin/env python3
"""
write a measure_runtime coroutine that will execute
async_comprehension four times in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run time for four parallel comprehensions"""
    start_time = time.time()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    return end_time - start_time
