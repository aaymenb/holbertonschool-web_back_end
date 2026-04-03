#!/usr/bin/env python3
"""
Module pour la gestion du cache avec Redis et historique des appels.
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Décorateur pour compter le nombre d'appels d'une méthode."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Incrémente le compteur dans Redis et retourne le résultat."""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Décorateur pour stocker l'historique des entrées et sorties."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Enregistre les arguments et le résultat dans des listes Redis."""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)

        return output
    return wrapper


def replay(method: Callable):
    """
    Affiche l'historique des appels d'une fonction spécifique.
    """
    # On récupère l'instance Redis via l'attribut __self__ de la méthode liée
    r = method.__self__._redis
    method_name = method.__qualname__

    inputs = r.lrange(f"{method_name}:inputs", 0, -1)
    outputs = r.lrange(f"{method_name}:outputs", 0, -1)

    print(f"{method_name} was called {len(inputs)} times:")

    for inp, out in zip(inputs, outputs):
        # On décode les bytes en string pour l'affichage
        print(f"{method_name}(*{inp.decode('utf-8')}) -> {out.decode('utf-8')}")


class Cache:
    """Classe Cache pour interagir avec Redis."""

    def __init__(self):
        """Initialise le client Redis et vide la base de données."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Génère une clé aléatoire et stocke la donnée dans Redis."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """Récupère une donnée et applique éventuellement une conversion."""
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """Récupère une string."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Récupère un entier."""
        return self.get(key, fn=int)
