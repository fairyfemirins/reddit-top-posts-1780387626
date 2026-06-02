#!/usr/bin/env python3
"""
Fetch the top post from a list of subreddits using the Reddit API.
Usage: python3 fetch_top_posts.py <subreddits_file> <output_file>
"""

import sys
import json
import time
import requests
from typing import List, Dict, Optional


def fetch_top_post(subreddit: str) -> Optional[Dict]:
    """Fetch the top post for a given subreddit."""
    url = f"https://old.reddit.com/r/{subreddit}/top.json?t=all&limit=1"
    headers = {"User-Agent": "Femirins/1.0 (Autonomous Agent)"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data["data"]["children"]:
            post = data["data"]["children"][0]["data"]
            return {
                "subreddit": subreddit,
                "title": post["title"],
                "url": f"https://reddit.com{post['permalink']}",
                "score": post["score"],
                "author": post["author"]
            }
    except Exception as e:
        print(f"Error fetching {subreddit}: {e}", file=sys.stderr)
    return None


def load_subreddits(file_path: str) -> List[str]:
    """Load a list of subreddits from a file."""
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 fetch_top_posts.py <subreddits_file> <output_file>")
        sys.exit(1)
    
    subreddits_file = sys.argv[1]
    output_file = sys.argv[2]
    
    subreddits = load_subreddits(subreddits_file)
    results = []
    
    for subreddit in subreddits:
        post = fetch_top_post(subreddit)
        if post:
            results.append(post)
            print(f"Fetched: {subreddit}")
        time.sleep(2)  # Avoid rate limits
    
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved {len(results)} posts to {output_file}")


if __name__ == "__main__":
    main()