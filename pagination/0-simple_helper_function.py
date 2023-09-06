#!/usr/bin/env python3
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    last_page = page * page_size
    first_page = last_page - page_size
    return (first_page, last_page)
