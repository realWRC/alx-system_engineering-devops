#!/usr/bin/python3
"""Module that queries the reddit api"""


def top_ten(subreddit):
    """
    script that queries the Reddit API and returns the top 10 hot post
    to the subreddit
    """
    import requests

    query_info = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                              .format(subreddit),
                              headers={"User-Agent": "My-Agent"},
                              allow_redirects=False)
    if query_info.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in query_info.json().get("data").get("children")]
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
#     if subreddit is None or not isinstance(subreddit, str):
#         print("None")
#
#     browser = {'User-Agent': 'Google Chrome Version 127.0.6533.100'}
#     url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
#     params = {
#             "limit": 10
#             }
#     response = requests.get(
#             url, headers=browser, params=params, allow_redirects=False
#             )
#
#     if response.status_code == 404:
#         print("None")
#         return
#
#     result = response.json()
#     try:
#         for i in range(0, 10):
#             post = result.get('data').get('children')[i].get('data')\
#                     .get('title')
#             print(post)
#
#     except Exception:
#         print("None")
