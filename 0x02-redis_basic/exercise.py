#!/usr/bin/env python3
"""
Cache class for writing strings to Redis
"""
from typing import Callable, Union
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using a random key and return the key.

        Args:
            data (Union[str, bytes, int, float]): Input data to be stored.

        Returns:
            str: Randomly generated key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


if __name__ == "__main__":
    cache = Cache()
    data = b"hello"
    key = cache.store(data)
    print(key)
    local_redis = redis.Redis()
    print(local_redis.get(key))

# Reading from Redis and recovering original type
    """
Cache class for reading from Redis and recovering original type
"""


class Cache:
    def __init__(self):
        self._redis = redis.Redis()

    def get(self,
            key: str,
            fn: Callable = None) -> Union[str,
                                          bytes,
                                          int,
                                          float]:
        """
        Retrieve data from Redis using the specified key

        Args:
            key (str): The key to retrieve data from Redis.
            fn (Callable): Optional callable function to convert the data.

        Returns:
            Union: Retrieved data, possibly converted by the provided function.
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Shortcut method to retrieve a string from Redis.

        Args:
            key (str): The key to retrieve the string from Redis.

        Returns:
            str: Retrieved string.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Shortcut method to retrieve an integer from Redis.

        Args:
            key (str): The key to retrieve the integer from Redis.

        Returns:
            int: Retrieved integer.
        """
        return self.get(key, fn=int)


if __name__ == "__main__":
    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value
