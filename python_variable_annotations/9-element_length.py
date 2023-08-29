#!/usr/bin/env python3
"""imports"""
from typing import Iterable, List, Sequence, Tuple
"""
takes list and return sum
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    sum list
    """
    return ([(i, len(i)) for i in lst])
