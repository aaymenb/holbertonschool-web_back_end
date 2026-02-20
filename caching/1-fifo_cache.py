def put(self, key, item):
    """ Méthode put corrigée pour le checker """
    if key is None or item is None:
        return

    # Si la clé est déjà là, on la supprime de la liste d'ordre 
    # pour la remettre à la fin (ou on ne touche pas à l'ordre, 
    # selon l'interprétation stricte du FIFO)
    if key in self.cache_data:
        self.keys_order.remove(key)

    self.cache_data[key] = item
    self.keys_order.append(key)

    # On vérifie si on dépasse la limite
    if len(self.cache_data) > BaseCaching.MAX_ITEMS:
        # On récupère le premier élément (le plus vieux)
        discarded_key = self.keys_order.pop(0)
        del self.cache_data[discarded_key]
        print("DISCARD: {}".format(discarded_key))
