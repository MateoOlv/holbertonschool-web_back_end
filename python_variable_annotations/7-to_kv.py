#!/usr/bin/env python3
"""imports"""
from typing import Union, Tuple
"""
takes list and return sum
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """sum list"""
    return (k, float(v * v))
