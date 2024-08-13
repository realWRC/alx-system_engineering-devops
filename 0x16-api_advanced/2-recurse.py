#!/usr/bin/python3
"""
Defines function top_ten.
"""

import requests


def recurse(subreddit, hot_list=None, page=None):
    """
    Function that queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.
    """
    if hot_list is None:
        hot_list = []

    user_agent = {'User-Agent': 'api_advanced-project'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    parameters = {'after': page}
    response = requests.get(
            url,
            params=parameters,
            headers=user_agent,
            allow_redirects=False
            )

    if response.status_code == 200:
        result = response.json().get("data")
        if result:
            titles = [child.get("data").get("title") for child in result.get("children", [])]
            hot_list.extend(titles)

            page = result.get("after")
            if page:
                return recurse(subreddit, hot_list, page)
            else:
                return hot_list
    return None
