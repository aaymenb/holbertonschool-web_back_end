#!/usr/bin/python3
""" FIFO caching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines a FIFO caching system
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        # Si la clé est NOUVELLE, on l'ajoute à la liste de suivi
        if key not in self.cache_data:
            self.keys_order.append(key)
        
        # On met à jour ou on ajoute dans le dictionnaire
        self.cache_data[key] = item

        # On vérifie si on dépasse la limite
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # On prend le premier élément de la liste (le plus vieux)
            discarded_key = self.keys_order.pop(0)
            del self.cache_data[discarded_key]
            print("DISCARD: {}".format(discarded_key))

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
