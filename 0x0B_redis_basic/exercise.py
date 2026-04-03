#!/usr/bin/env python3
"""
This module implements a Cache class with call tracking and a replay function.
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator that counts how many times a method is called."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Increments the counter in Redis."""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a function."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Pushes input arguments and output results to Redis lists."""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)

        return output
    return wrapper


def replay(method: Callable):
    """
    Displays the history of calls of a particular function.
    """
    # Access the Redis instance from the method's self (the class instance)
    # method is a bound method, so .__self__ refers to the Cache instance
    self_instance = method.__self__
    r = self_instance._redis
    
    method_name = method.__qualname__
    inputs_key = f"{method_name}:inputs"
    outputs_key = f"{method_name}:outputs"
    
    # Retrieve all elements from both lists (0 to -1)
    inputs = r.lrange(inputs_key, 0, -1)
    outputs = r.lrange(outputs_key, 0, -1)
    
    # Format the summary line
    print(f"{method_name} was called {len(inputs)} times:")
    
    # Use zip to iterate through both lists simultaneously
    for inp, out in zip(inputs, outputs):
        # Decode byte strings from Redis to UTF-8 for printing
        input_str = inp.decode("utf-8")
        output_str = out.decode("utf-8")
        print(f"{method_name}(*{input_str}) -> {output_str}")


class Cache:
    """A Cache class to interact with a Redis database."""

    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates a random key and stores data in Redis."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """Retrieves data and optionally applies conversion."""
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """Decodes Redis bytes back to a string."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Converts Redis bytes back to an integer."""
        return self.get(key, fn=int)
