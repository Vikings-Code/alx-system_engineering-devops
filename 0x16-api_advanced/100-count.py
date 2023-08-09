#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""

import requests

def count_words(subreddit, word_list, after='', word_dict=None):
    """Queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords.
    
    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of keywords to search for in post titles.
        after (str): The parameter for the next page of the API results.
        word_dict (dict): Key/value pairs of keywords/counts.
    """
    if word_dict is None:
        word_dict = {word.lower(): 0 for word in word_list}
    
    if after is None:
        sorted_words = sorted(
            word_dict.items(),
            key=lambda x: (-x[1], x[0])
        )
        for word, count in sorted_words:
            if count:
                print(f"{word}: {count}")
        return None
    
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "redquery"
    }
    params = {
        "limit": 100,
        "after": after
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        return None
    
    try:
        data = response.json()["data"]
        hot = data["children"]
        aft = data["after"]
        for post in hot:
            title = post["data"]["title"]
            lower = [word.lower() for word in title.split()]
            
            for word in word_dict.keys():
                word_dict[word] += lower.count(word)
    
    except Exception:
        return None
    
    count_words(subreddit, word_list, aft, word_dict)
