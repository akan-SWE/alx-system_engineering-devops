#!/usr/bin/python3
"""
Module for counting and displaying word occurrences in the hot articles
of a specified subreddit using the Reddit API. Words are counted across
all pages and results are presented in descending order by count, with
alphabetical sorting for words with the same count.
"""
from collections import Counter
import re
import requests


def count_words(subreddit, word_list, after=None, stats={}):
    """
    Count all occurrences of words in the hot articles from the Reddit API.

    The result is printed in descending order by word count.
    If multiple words have the same count, they are sorted alphabetically
    in ascending order (A to Z).
    """
    # initial stats
    stats = {word: 0 for word in word_list}
    # Add boundaries to each word
    word_list_ = [r'\b' + word + r'\b' for word in word_list]

    count_words_helper(subreddit, word_list_, after, stats)
    print_result(stats)  # print stats


def count_words_helper(subreddit, word_list, after=None, stats={}):
    """
    Count the occurrences of each word in the hot articles of a subreddit
    for a specific page or listing returned by the Reddit API.

    The results contribute to a cumulative count across all pages processed.
    """
    after = f'?after={after}' if after else ''
    url = f'https://www.reddit.com/r/{subreddit}/hot.json{after}'
    header = {'User-Agent': '100-count.py/0.1 by alx'}
    res = requests.get(url, headers=header, allow_redirects=False)

    if res.status_code == 200:
        res_data = res.json()['data']
        after = res_data['after']

        for article in res_data['children']:
            title = article['data']['title']  # title of the article
            patterns = '|'.join(word_list)
            # find all occurence of word in the title
            result = re.findall(patterns, title, flags=re.IGNORECASE)
            # map each word in lower case to the actual word
            word_dict = {_.strip(r'\b').lower(): _.strip(r'\b')
                         for _ in word_list}
            # count the occurence of word in the result
            result_counter = Counter([word.lower() for word in result])

            # update the stats of each word
            for word, count in result_counter.items():
                stats[word_dict[word]] += count

        # Move to the next listing
        count_words_helper(subreddit, word_list, after, stats)
    else:
        return


def print_result(stats):
    """
    Print the word count statistics in descending order by count.
    If multiple words have the same count, they are sorted
    alphabetically in ascending order.
    """
    for word, count in sorted(stats, key=lambda x: (-x[-1], x[0])):
        print(f'{word}: {count}')
