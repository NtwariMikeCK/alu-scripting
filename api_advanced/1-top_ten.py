#!/usr/bin/python3
"""Script that fetches the titles of 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints 'None'.
    """
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(subreddit_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        json_data = response.json()
        # Get the first 10 posts
        posts = json_data.get('data', {}).get('children', [])
        if posts:
            for i in range(min(10, len(posts))):  # Print available titles, up to 10
                print(posts[i].get('data', {}).get('title'))
            print("OK")  # Print "OK" after successfully displaying titles
        else:
            print("None")
    else:
        print("None")
