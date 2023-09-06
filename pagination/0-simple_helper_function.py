#!/usr/bin/env python3
"""Imports"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """get first and last page"""
    last_page = page * page_size
    first_page = last_page - page_size
    return (first_page, last_page)
