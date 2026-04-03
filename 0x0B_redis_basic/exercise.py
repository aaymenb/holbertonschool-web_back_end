#!/usr/bin/env python3
"""
This module provides a Cache class for basic Redis operations.
"""
import redis
import uuid
from typing import Union


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
        Generates a random key, stores the input data in Redis 
        using that key, and returns the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
