#!/usr/bin/python3
"""
Defines function number_of_subscribers.
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return (0)

    browser = {'User-Agent': 'Google Chrome Version 127.0.6533.100'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=browser)
    result = response.json()
    return result.get('data').get('subscribers')
    try:
        return result.get('data').get('subscribers')
    except Exception as e:
        return (0)
