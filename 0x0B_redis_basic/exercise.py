#!/usr/bin/env python3
"""
This module expands the Cache class to handle data retrieval
and type conversion from Redis.
"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """
    A Cache class to interact with a Redis database.
    """

    def __init__(self):
        """
        Initialize the Redis client and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key, stores the input data in Redis,
        and returns the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieves data from Redis and optionally applies a 
        conversion function.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Automatically parametrizes Cache.get to return a string.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Automatically parametrizes Cache.get to return an integer.
        """
        return self.get(key, fn=int)
