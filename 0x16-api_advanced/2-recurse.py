#!/usr/bin/python3
"""queries the Reddit API and returns a list containing the titles
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    if hot_list is None:
        hot_list = []
    headers = {'User-Agent': 'MaryanneNgaruiya/1.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100}
    if after:
        params['after'] = after
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return None
    data = response.json()['data']
    for child in data['children']:
        hot_list.append(child['data']['title'])
    if data['after'] is not None:
        recurse(subreddit, hot_list, data['after'])
    return hot_list
