"""
Hacker News Scraper
Scrapes the Hacker News front page and displays top stories.

Usage:
    python hackernews_scraper.py [--limit N] [--min-score SCORE] [--json]

Requirements:
    pip install requests beautifulsoup4
"""

import argparse
import json
import sys
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

HN_URL = "https://news.ycombinator.com/"


def scrape_hn(limit=30, min_score=0):
    """Scrape Hacker News front page stories."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    response = requests.get(HN_URL, headers=headers, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    stories = []

    # Each story is a table row with class "athing"
    story_rows = soup.find_all("tr", class_="athing")

    for row in story_rows:
        story_data = {}

        # Story ID
        story_data["id"] = row.get("id", "")

        # Title and URL
        title_cell = row.find("td", class_="title")
        if title_cell:
            title_link = title_cell.find("a")
            if title_link:
                story_data["title"] = title_link.get_text(strip=True)
                story_data["url"] = title_link.get("href", "")
                # Handle relative URLs (e.g., item?id=xxx)
                if story_data["url"].startswith("item?"):
                    story_data["url"] = urljoin(HN_URL, story_data["url"])

        # Get the subtext row (next sibling)
        subtext_row = row.find_next_sibling("tr")
        if subtext_row:
            subtext = subtext_row.find("td", class_="subtext")
            if subtext:
                # Score
                score_elem = subtext.find("span", class_="score")
                if score_elem:
                    score_text = score_elem.get_text(strip=True)
                    story_data["score"] = int(score_text.split()[0]) if score_text else 0
                else:
                    story_data["score"] = 0

                # Author
                author_elem = subtext.find("a", class_="hnuser")
                story_data["author"] = author_elem.get_text(strip=True) if author_elem else "N/A"

                # Comments link
                comments_link = subtext.find("a", href=lambda x: x and "item?id=" in x)
                story_data["comments"] = comments_link.get_text(strip=True) if comments_link else "0 comments"
                story_data["comments_url"] = urljoin(HN_URL, comments_link["href"]) if comments_link else ""

        # Filter by minimum score
        if story_data.get("score", 0) >= min_score:
            stories.append(story_data)

        if len(stories) >= limit:
            break

    return stories


def display_stories(stories):
    """Display stories in a formatted way."""
    if not stories:
        print("No stories found matching criteria.")
        return

    print(f"\n{'='*80}")
    print(f"  Hacker News Top Stories ({len(stories)} stories)")
    print(f"{'='*80}\n")

    for i, story in enumerate(stories, 1):
        print(f"  {i}. {story.get('title', 'N/A')}")
        print(f"     ⬆️  {story.get('score', 0)} points | 👤 {story.get('author', 'N/A')} | 💬 {story.get('comments', 'N/A')}")
        print(f"     🔗 {story.get('url', 'N/A')}")
        print(f"     💬 Discuss: {story.get('comments_url', 'N/A')}")
        print()


def main():
    parser = argparse.ArgumentParser(
        description="Scrape Hacker News front page"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=30,
        help="Maximum number of stories to display (default: 30)",
    )
    parser.add_argument(
        "--min-score",
        type=int,
        default=0,
        help="Minimum score threshold (default: 0)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON instead of formatted text",
    )
    args = parser.parse_args()

    try:
        stories = scrape_hn(limit=args.limit, min_score=args.min_score)

        if args.json:
            print(json.dumps(stories, indent=2))
        else:
            display_stories(stories)
    except requests.RequestException as e:
        print(f"Error fetching data: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()