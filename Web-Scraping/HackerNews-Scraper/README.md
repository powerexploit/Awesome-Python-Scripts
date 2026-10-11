# Hacker News Scraper

Scrapes the Hacker News front page and displays top stories with scores, authors, and comment links.

## Features

- Fetches top stories from Hacker News
- Displays story title, URL, score, author, and comments
- Filter by minimum score threshold
- Output as formatted text or JSON
- Includes discussion links

## Usage

```bash
# Basic usage (top 30 stories)
python hackernews_scraper.py

# Limit number of stories
python hackernews_scraper.py --limit 10

# Filter by minimum score
python hackernews_scraper.py --min-score 100

# Output as JSON
python hackernews_scraper.py --json

# Combined options
python hackernews_scraper.py --limit 20 --min-score 50 --json
```

## Output Example

```
================================================================================
  Hacker News Top Stories (30 stories)
================================================================================

  1. Show HN: A new open-source project
     ⬆️  234 points | 👤 devuser | 💬 45 comments
     🔗 https://example.com/project
     💬 Discuss: https://news.ycombinator.com/item?id=12345678
```

## JSON Output

Use `--json` flag for machine-readable output:

```bash
python hackernews_scraper.py --limit 5 --json
```

## Requirements

- Python 3.6+
- `requests`
- `beautifulsoup4`

Install dependencies:

```bash
pip install requests beautifulsoup4
```