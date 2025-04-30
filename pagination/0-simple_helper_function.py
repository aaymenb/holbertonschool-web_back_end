#!/usr/bin/env python3
"""
This module provides a helper function for pagination.

The `index_range` function calculates the start and end indices
for a given page and page size, which are useful for slicing
data in paginated systems.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for a given page and page size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index (inclusive)
        and the end index (exclusive).
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
