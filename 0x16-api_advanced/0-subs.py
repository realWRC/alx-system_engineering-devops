#!/usr/bin/python3
"""
Defines function number_of_subscribers: Function that queries the Reddit
API and returns the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return (0)

    browser = {'User-Agent': 'Google Chrome Version 127.0.6533.100'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=browser, allow_redirects=False)
    result = response.json()

    try:
        return result.get('data').get('subscribers')
    except Exception:
        return (0)


if __name__ == "__main__":
    pass
