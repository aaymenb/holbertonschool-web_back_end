#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get hypermedia pagination information based on index.

        Args:
            index (int): The start index of the return page
            page_size (int): The number of items per page

        Returns:
            Dict: A dictionary containing pagination information
        """
        indexed_dataset = self.indexed_dataset()
        assert (index is None or
               (isinstance(index, int) and index < len(indexed_dataset))), \
            "index out of range"

        if index is None:
            index = 0

        data = []
        next_index = index

        # Get the data for the current page
        for i in range(page_size):
            if next_index in indexed_dataset:
                data.append(indexed_dataset[next_index])
                next_index += 1
            else:
                break

        next_idx = next_index if next_index < len(indexed_dataset) else None
        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_idx
        }
