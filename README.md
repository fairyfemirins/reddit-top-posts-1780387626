# Reddit Top Posts Explorer

A static web page that lists the top post from all subreddits. Inspired by [this r/SomebodyMakeThis post](https://www.reddit.com/r/SomebodyMakeThis/comments/1awvfn/smt_a_page_that_lists_the_top_1_post_from_all/).

## Problem
- Reddit's default "top" pages are dominated by a few large subreddits.
- Users miss out on high-quality content from smaller or niche subreddits.
- No existing tool provides a consolidated, browsable list of the top post from every subreddit.

## Solution
- Fetch the top post from a list of subreddits using the Reddit API.
- Display the results in a static HTML page for easy browsing.

## Technical Architecture
1. **Data Fetching:**
   - Use the Reddit API (`/r/{subreddit}/top.json?t=all&limit=1`) to fetch the top post for each subreddit.
   - Fallback to `old.reddit.com` if the main API blocks requests.
   - Handle rate limits and errors gracefully.

2. **Data Storage:**
   - Cache results in JSON for performance.

3. **Display:**
   - Generate a static HTML page with the top post from each subreddit.
   - Include subreddit name, post title, URL, score, and author.

## Limitations
- **Reddit API Blocking:** The Reddit API may block unauthenticated requests. This prototype uses `old.reddit.com` as a fallback.
- **Rate Limits:** The Reddit API enforces rate limits (e.g., 60 requests per minute). This prototype includes a 2-second delay between requests.
- **Subreddit List:** This prototype uses a static list of subreddits. A production version would need a dynamic or more comprehensive list.

## How to Use
1. Clone this repository:
   ```bash
   git clone https://github.com/fairyfemirins/reddit-top-posts-1780387626.git
   ```
2. Open `index.html` in a web browser.

## Transfer Instructions
This repository was published under the `fairyfemirins` namespace due to GitHub API restrictions. To transfer it to the `Femirins` namespace:

1. **Fork the Repository:**
   - Visit [https://github.com/fairyfemirins/reddit-top-posts-1780387626](https://github.com/fairyfemirins/reddit-top-posts-1780387626).
   - Click "Fork" and select the `Femirins` namespace.

2. **Clone the Fork:**
   ```bash
   git clone https://github.com/Femirins/reddit-top-posts.git
   ```

3. **Update Remote URL (Optional):**
   ```bash
   git remote set-url origin https://github.com/Femirins/reddit-top-posts.git
   ```

## Future Work
- **Authentication:** Use Reddit OAuth to avoid API blocking.
- **Dynamic Subreddit List:** Fetch a dynamic list of subreddits from `r/ListOfSubreddits`.
- **Hosting:** Deploy the static site to GitHub Pages or Netlify.
- **Automation:** Set up a cron job to update the top posts daily.

## License
This project is licensed under the MIT License.