#!/usr/bin/python3
"""
This module defines a function for querying the Reddit API to fetch the number 
of subscribers for a specified subreddit.

Functions:
    number_of_subscribers(subreddit): Returns the total number of subscribers 
    for a given subreddit or 0 if the subreddit is invalid.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to retrieve the number of subscribers for a given subreddit.
    
    The function sends a GET request to the Reddit API to obtain information about 
    the specified subreddit. If the subreddit is valid, it returns the total number 
    of subscribers. If the subreddit is invalid or any error occurs, the function 
    returns 0. Redirects are disabled to accurately identify invalid subreddits.
    
    Args:
        subreddit (str): The name of the subreddit to query.
    
    Returns:
        int: The number of subscribers for the subreddit, or 0 if the subreddit is invalid.
    
    Usage Example:
        >>> number_of_subscribers("programming")
        756024
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "custom-user-agent"}  # Avoids rate limits

    try:
        # Perform GET request with no redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the subreddit is valid (status code 200)
        if response.status_code == 200:
            data = response.json().get("data", {})
            return data.get("subscribers", 0)
        else:
            return 0
    except requests.RequestException:
        return 0
