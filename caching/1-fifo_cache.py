#!/usr/bin/python3
""" FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache defines a caching system with a FIFO eviction policy.
    Inherits from BaseCaching.
    """

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """
        Add an item in the cache.
        If the cache exceeds MAX_ITEMS, the oldest item (FIFO) is discarded.
        """
        if key is None or item is None:
            return

        # If key already exists, we update it but don't change its FIFO position
        if key not in self.cache_data:
            self.keys_order.append(key)

        self.cache_data[key] = item

        # Check if we exceeded the limit defined in BaseCaching
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Pop the first key added (index 0)
            discarded_key = self.keys_order.pop(0)
            del self.cache_data[discarded_key]
            print("DISCARD: {}".format(discarded_key))

    def get(self, key):
        """
        Get an item by key.
        Returns the value in self.cache_data linked to key.
        """
        return self.cache_data.get(key)
