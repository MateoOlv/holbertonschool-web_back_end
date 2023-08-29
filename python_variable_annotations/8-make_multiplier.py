#!/usr/bin/env python3
"""imports"""
from typing import Callable
"""
takes list and return sum
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    sum list
    """
    def mfunction(n: float) -> float:
        """
        comment
        """
        return n * multiplier
    return mfunction
