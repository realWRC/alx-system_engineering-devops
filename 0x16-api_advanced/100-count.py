#!/usr/bin/python3
"""
Function that queries the Reddit API.
"""

import requests
from collections import Counter


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Queries the Reddit API recursively, parses the titles of all hot articles,
    and prints a sorted count of given keywords (case-insensitive).
    """
    if counts is None:
        counts = Counter()
    if after is None:
        word_list = [word.lower() for word in word_list]
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}
    response = requests.get(
            url, headers=user_agent, params=params, allow_redirects=False
            )

    if response.status_code != 200:
        return

    data = response.json().get('data', {})
    after = data.get('after')

    for child in data.get('children', []):
        title = child.get('data', {}).get('title', '').lower()
        words_in_title = title.split()
        for word in word_list:
            counts[word] += words_in_title.count(word)

    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        if counts:
            for word, count in sorted(
                    counts.items(), key=lambda item: (-item[1], item[0])
                    ):
                if count > 0:
                    print("{}: {}".format(word, count))
