#!/usr/bin/env python3
"""imports"""
import typing
from asyncio import run
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """function"""
    start = time.time()
    run(wait_n(n, max_delay))
    end = time.time()
    stime = end - start
    return stime / n
