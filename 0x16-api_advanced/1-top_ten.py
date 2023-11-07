#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """function to get the first 10 post of a given sub reddit
    """
    headers = {"User-Agent": "Mozilla/5.0"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for i in range(10):
            print(posts[i]['data']['title'])
    else:
        print(None)
