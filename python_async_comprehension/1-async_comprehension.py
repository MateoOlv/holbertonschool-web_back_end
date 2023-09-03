#!/usr/bin/env python3
"""
imports module
"""
from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """function"""
    return [item async for item in async_generator()]
