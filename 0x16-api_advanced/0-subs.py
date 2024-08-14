#!/usr/bin/python3
"""
Module: 0-subs.py

This module defines a function to get the number of subscribers
for a given subreddit using the Reddit API.
"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers to the subreddit"""

    header = {'User-Agent': '0-subs/0.1 by alx'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    res = requests.get(url, allow_redirects=False, headers=header)

    if res.status_code == 200:
        return res.json().get('data', {}).get('subscribers', 0)
    else:
        return 0
