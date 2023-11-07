#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers
If an invalid subreddit is given, the function should return 0.
"""

import requests
def number_of_subscribers(subreddit):
    """ get the number of subscribers of a subreddit"""
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
