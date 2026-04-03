#!/usr/bin/env python3
"""
Module de gestion de cache Redis
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Compte le nombre d'appels à une méthode """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Incrémente et appelle la méthode d'origine """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Stocke l'historique des entrées et sorties """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Ajoute les inputs/outputs dans des listes Redis """
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))

        return output
    return wrapper


def replay(method: Callable):
    """ Affiche l'historique complet des appels """
    # Récupération de l'instance redis via la méthode liée
    r = method.__self__._redis
    name = method.__qualname__
    
    # Récupération des données
    inputs = r.lrange(f"{name}:inputs", 0, -1)
    outputs = r.lrange(f"{name}:outputs", 0, -1)
    
    # Affichage de l'en-tête (Vérifiez bien le texte exact)
    print(f"{name} was called {len(inputs)} times:")
    
    # Boucle de rendu
    for inp, out in zip(inputs, outputs):
        # On décode les bytes retournés par Redis
        # On ajoute manuellement l'astérisque '*' avant les parenthèses de l'input
        print(f"{name}(*{inp.decode('utf-8')}) -> {out.decode('utf-8')}")


class Cache:
    """ Classe de mise en cache """
    def __init__(self):
        """ Initialisation """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history  # Call history en premier (plus haut)
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Stocke une donnée """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> any:
        """ Récupère une donnée """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """ Helper string """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """ Helper int """
        return self.get(key, int)
