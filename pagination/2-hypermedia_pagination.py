#!/usr/bin/env python3
"""
Hypermedia pagination implementation
"""
import csv
import math
from typing import List, Dict

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of data from the dataset.

        Args:
            page (int): The page number (1-indexed)
            page_size (int): The number of items per page

        Returns:
            List[List]: A list of rows for the requested page
        """
        assert isinstance(page, int) and page > 0, "page must be positive"
        assert isinstance(page_size, int) and page_size > 0, "page_size > 0"

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Get hypermedia pagination information.

        Args:
            page (int): The page number (1-indexed)
            page_size (int): The number of items per page

        Returns:
            Dict: A dictionary containing pagination information
        """
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)

        # Get the page data
        page_data = self.get_page(page, page_size)

        # Determine next and previous pages
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
