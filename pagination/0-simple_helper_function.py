#!/usr/bin/env python3
"""
Write a function named index_range that takes two integer arguments page and
page_size. The function should return a tuple of size two containing a start
index and an end index corresponding to the range of indexes to return in a
list for those particular pagination parameters. Page numbers are 1-indexed,
i.e. the first page is page 1.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for pagination.

    Args:
        page (int): The page number (1-indexed)
        page_size (int): The number of items per page

    Returns:
        Tuple[int, int]: A tuple containing the start and end indices
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
