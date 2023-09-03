#!/usr/bin/env python3
"""
imports
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    function
    """
    time = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
