#!/usr/bin/python3
"""
Defines function top_ten: Function that queries the Reddit API and
prints the titles of the first 10 hot posts listed for a
given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    browser = {'User-Agent': 'Google Chrome Version 127.0.6533.100'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(
            url, headers=browser, allow_redirects=False
            )
    result = response.json()
    try:
        for i in range(0, 10):
            post = result.get('data').get('children')[i].get('data')\
                    .get('title')
            print(post)

    except Exception:
        print("None")
# #!/usr/bin/python3
# """
# Defines function top_ten: Function that queries the Reddit API and
# prints the titles of the first 10 hot posts listed for a
# given subreddit.
# """
#
# import requests
#
#
# def top_ten(subreddit):
#     """
#     Function that queries the Reddit API and prints the titles of the
#     first 10 hot posts listed for a given subreddit.
#     """
#     user_agent = {'User-Agent': 'api_advanced-project'}
#     url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
#     params = {"limit": 10}
#     response = requests.get(
#             url, headers=user_agent, params=params, allow_redirects=False
#             )
#     try:
#         response.raise_for_status()
#         result = response.json()
#     except requests.exceptions.HTTPError as http_err:
#         # print("HTTP error occurred: {}".format(http_err))
#         print("None")
#         return
#     except requests.exceptions.RequestException as req_err:
#         # print("Error occurred: {}".format(req_err))
#         print("None")
#         return
#     except ValueError:
#         # print("Response content is not valid JSON or is empty.")
#         print("None")
#         return
#
#     if result.get("data"):
#         for child in result.get("data").get("children", []):
#             print(child.get("data").get("title"))
#     else:
#         print("None")
#         return
