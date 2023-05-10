"""
Redis basic.
"""
from typing import Union, Callable, Optional
from functools import wraps
import redis
import uuid


def call_history(method: Callable) -> Callable:
    """Decorator that stores the history of inputs and outputs for a particular
function.

    Args:
        method: The function to be decorated.

    Returns:
        The decorated function.
    """
    method_key = method.__qualname__
    inputs, outputs = method_key + ':inputs', method_key + ':outputs'

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to store the input and output of the decorated
function."""
        self._redis.rpush(inputs, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(result))
        return result

    return wrapper


def count_calls(method: Callable) -> Callable:
    """Decorator that creates and returns a function which increments the
count \
        for that key every time the method is called and returns the value
returned by the original method.

    Args:
        method: The function to be decorated.

    Returns:
        The decorated function.
    """
    method_key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to increment the count and call the decorated
function."""
        self._redis.incr(method_key)
        return method(self, *args, **kwargs)

    return wrapper


def replay(method: Callable) -> None:
    """Displays the history of calls of a particular function.

    Args:
        method: The function whose call history is to be displayed.

    Returns:
        None.
    """
    method_key = method.__qualname__
    inputs, outputs = method_key + ':inputs', method_key + ':outputs'
    redis = method.__self__._redis
    method_count = redis.get(method_key).decode('utf-8')
    print(f'{method_key} was called {method_count} times:')
    IOTuple = zip(redis.lrange(inputs, 0, -1), redis.lrange(outputs, 0, -1))
    for inp, outp in list(IOTuple):
        attr, data = inp.decode("utf-8"), outp.decode("utf-8")
        print(f'{method_key}(*{attr}) -> {data}')


class Cache:
    """Cache class to handle redis operations."""

    def __init__(self):
        """Initializes an instance of the Cache class with an instance of the
Redis client."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores the given data in Redis and returns a unique key.

        Args:
            data: The data to be stored.

        Returns:
            A unique key to retrieve the stored data.
        """
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key

    def get(self,
            key: str, fn: Optional[Callable] = None) -> str:
        """Retrieves the data from Redis corresponding to the given key, \
            and converts it to the desired format using the given function.

        Args:
            key: The key of the data to be retrieved.
            fn: Optional. Function to convert retrieved data to desired format.

        Returns:
            The retrieved data in the desired format.
        """
        data = self._redis.get(key)
        return fn(data)
