#!/usr/bin/python3
"""
Module to fetch the number of subscribers for a given subreddit
using the Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit.

    Returns:
    int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0