#!/usr/bin/python3
""" FIFO caching module """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines a FIFO caching system """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        # Si la clé est déjà là, on ne l'ajoute pas à la liste d'ordre
        # (elle garde sa place de "vieille" clé)
        if key not in self.cache_data:
            self.keys_order.append(key)
        
        self.cache_data[key] = item

        # On vérifie la limite APRÈS l'ajout
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # On retire le premier de la liste (le plus ancien)
            first_key = self.keys_order.pop(0)
            del self.cache_data[first_key]
            print("DISCARD: {}".format(first_key))

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key)
