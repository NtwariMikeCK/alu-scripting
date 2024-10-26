#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
    
    If the subreddit is invalid, it prints 'None'.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "custom-user-agent"}
    params = {"limit": 10}  # Limit the result to 10 posts

    try:
        # Perform GET request without following redirects
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        # Check if the subreddit is valid (status code 200)
        if response.status_code == 200:
            data = response.json().get("data", {}).get("children", [])
            # Print the title of each post
            for post in data:
                print(post.get("data", {}).get("title"))
        else:
            print("None")
    except requests.RequestException:
        print("None")
