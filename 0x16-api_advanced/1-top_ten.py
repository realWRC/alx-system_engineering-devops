#!/usr/bin/python3
"""
Defines function top_ten: Function that queries the Reddit API and
prints the titles of the first 10 hot posts listed for a
given subreddit.
"""

from requests import get


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    browser = {'User-Agent': 'Google Chrome Version 127.0.6533.100'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = get(url, headers=browser)
    result = response.json()
    try:
        for i in range(0, 10):
            post = result.get('data').get('children')[i].get('data')\
                    .get('title')
            print(post)

    except Exception:
        print("None")
