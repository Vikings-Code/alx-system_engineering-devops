#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    if (type(subreddit) is not str):
        return(0)
    url_api = ("https://www.reddit.com/r/{}/about.json".format(subreddit))
    headers = {'user-agent': 'safari:holberton/0.1.0'}
    response = requests.get(url_api, headers=headers)
    if response.status_code is not 200:
        return(0)
    return(response.json().get("data").get("subscribers"))
