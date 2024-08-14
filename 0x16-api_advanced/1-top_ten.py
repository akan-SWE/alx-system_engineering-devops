#!/usr/bin/python3
"""
Module: 1-top_ten

Defines a function to get the top 10 hot posts for a given
subreddit.
"""
from requests import get


def top_ten(subreddit):
    """
    Retrieve and print the titles of the top 10 hot posts for a subreddit.

    Args:
        subreddit (str): The name of the subreddit to fetch the top posts from.

    Prints:
        The titles of the top 10 hot posts. If the subreddit does not exist or
        an error occurs, 'None' is printed.
    """

    header = {'User-Agent': '0-subs/0.1 by alx'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    res = get(url, headers=header, allow_redirects=False)
    if res.status_code == 200:
        posts = res.json().get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))
    else:
        print('None')
