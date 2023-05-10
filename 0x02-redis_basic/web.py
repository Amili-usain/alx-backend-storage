#!/usr/bin/env python3
"""
This script implements a web cache that tracks the number of times a particular
URL has been accessed and caches the result with an expiration time of 10
seconds.
"""

import redis
import requests
from functools import wraps

# initialize Redis client
redis_client = redis.Redis()


def url_access_count(method):
    """Decorator function that counts how many times a URL is accessed"""
    @wraps(method)
    def wrapper(url):
        """Function that tracks URL access count and caches the result"""
        key = "cached:" + url
        cached_value = redis_client.get(key)

        if cached_value:
            return cached_value.decode("utf-8")

        # Get new content and update cache
        key_count = "count:" + url
        html_content = method(url)

        redis_client.incr(key_count)
        redis_client.setex(key, 10, html_content)
        return html_content

    return wrapper


@url_access_count
def get_page(url: str) -> str:
    """Function that obtains the HTML content of a particular URL"""
    results = requests.get(url)
    return results.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
