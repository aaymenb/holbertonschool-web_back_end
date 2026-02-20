#!/usr/bin/python3
""" FIFO caching module """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Système de mise en cache FIFO """

    def __init__(self):
        """ Initialisation """
        super().__init__()
        self.order = []  # Liste pour suivre l'ordre d'entrée exact

    def put(self, key, item):
        """ Ajoute un élément au cache """
        if key is None or item is None:
            return

        # Si la clé n'est pas déjà dans le cache, on l'ajoute à la file
        if key not in self.cache_data:
            self.order.append(key)
        
        self.cache_data[key] = item

        # Si on dépasse la limite
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # On récupère le plus ancien dans la liste 'order'
            discarded_key = self.order.pop(0)
            del self.cache_data[discarded_key]
            print("DISCARD: {}".format(discarded_key))

    def get(self, key):
        """ Récupère un élément du cache """
        return self.cache_data.get(key)
