#!/usr/bin/python3
""" LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines a LIFO caching system
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.last_key = ""

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        # Si le cache est plein et que la clé est nouvelle
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and \
                key not in self.cache_data:
                    # On utilise la dernière clé enregistrée
            if self.last_key:
                del self.cache_data[self.last_key]
                print("DISCARD: {}".format(self.last_key))

        self.cache_data[key] = item
        self.last_key = key

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
