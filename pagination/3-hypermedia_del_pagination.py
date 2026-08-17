#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination"""
import csv
from typing import Dict, List


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
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a dictionary with pagination metadata that stays
        consistent even if rows are deleted between two queries
        """
        data = self.indexed_dataset()
        assert index is None or (
            isinstance(index, int) and 0 <= index <= max(data.keys())
        )

        start = index or 0
        page_data = []
        next_index = start

        for i in range(start, max(data.keys()) + 1):
            if len(page_data) == page_size:
                break
            if i in data:
                page_data.append(data[i])
            next_index = i + 1

        return {
            'index': start,
            'next_index': next_index,
            'page_size': len(page_data),
            'data': page_data,
        }
        