#!/usr/bin/env python3
""" Module pour l'exercice Redis basic """
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Compte le nombre d'appels """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Incrémente la clé dans Redis """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Stocke l'historique des entrées/sorties """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Ajoute les arguments et le résultat dans des listes """
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))

        return output
    return wrapper


def replay(method: Callable):
    """ Affiche l'historique des appels d'une fonction """
    # Accès à l'instance redis via la méthode liée
    r = method.__self__._redis
    method_name = method.__qualname__
    
    inputs = r.lrange(f"{method_name}:inputs", 0, -1)
    outputs = r.lrange(f"{method_name}:outputs", 0, -1)
    
    # Formatage strict : "Cache.store was called X times:"
    print(f"{method_name} was called {len(inputs)} times:")
    
    for inp, out in zip(inputs, outputs):
        # On décode les bytes et on utilise le format exact de la consigne
        print(f"{method_name}(*{inp.decode('utf-8')}) -> {out.decode('utf-8')}")


class Cache:
    """ Classe Cache """
    def __init__(self):
        """ Init Redis """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history  # INDISPENSABLE : call_history en premier
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Stocke une valeur """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> any:
        """ Récupère une valeur """
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
