#!/usr/bin/python3
""" BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache defines a caching system without a limit.
    Inherits from BaseCaching which provides self.cache_data.
    """

    def put(self, key, item):
        """
        Add an item in the cache.
        If key or item is None, this method should not do anything.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key.
        Returns the value in self.cache_data linked to key.
        If key is None or doesn't exist, returns None.
        """
        return self.cache_data.get(key)
