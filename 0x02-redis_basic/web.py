# web.py

import requests
import redis
import time
from typing import Optional

# Initialize Redis connection
redis_conn = redis.Redis()


def get_page(url: str) -> str:
    """
    Retrieve HTML content of URL, track access count,
    and cache result with expiration.

    Args:
        url (str): The URL to retrieve HTML content from.

    Returns:
        str: The HTML content of the URL.
    """
    # Key to track access count for the URL
    count_key = f"count:{url}"

    # Increment access count
    access_count = redis_conn.incr(count_key)

    # Check if the HTML content is already cached
    cache_key = f"cache:{url}"
    cached_html = redis_conn.get(cache_key)

    if cached_html is not None:
        print(f"Cache hit for {url} ({access_count} accesses)")
        return cached_html.decode("utf-8")

    # Cache miss, fetch HTML content using requests
    print(f"Cache miss for {url} ({access_count} accesses)")

    # Simulate a slow response using http://slowwly.robertomurray.co.uk
    response = requests.get(
        f"http://slowwly.robertomurray.co.uk/delay/1000/url/{url}")

    # Extract HTML content
    html_content = response.text

    # Cache the HTML content with expiration time
    redis_conn.setex(cache_key, 10, html_content)

    return html_content


if __name__ == "__main__":
    # Test the get_page function
    url_to_test = "https://www.example.com"
    html_content = get_page(url_to_test)
    print(html_content)
