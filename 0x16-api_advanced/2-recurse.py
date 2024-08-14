#!/usr/bin/python3
"""
Module: 2-recurse

Function:
    recurse - Recursively queries the Reddit API to retrieve and return a list
    of titles for all hot articles in a given subreddit.
"""
from requests import get


def recurse(subreddit, hot_list=[], after=None):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    if after:
        url += f'?after={after}'

    res = get(url, allow_redirects=False, headers={
        'User-Agent': '2-recurse/0.1 alx'})
    if res.status_code == 200:
        data = res.json()['data']
        after = data['after']
        hot_list.extend([p['data']['title'] for p in data['children']])
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
