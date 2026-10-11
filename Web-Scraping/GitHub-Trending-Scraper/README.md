# GitHub Trending Scraper

Scrapes GitHub trending repositories and displays them in a clean, formatted output.

## Features

- Fetches trending repositories from GitHub
- Supports filtering by programming language
- Supports filtering by time period (daily, weekly, monthly)
- Displays repo name, description, stars, forks, language, and link

## Usage

```bash
# Basic usage
python github_trending.py

# Filter by language
python github_trending.py --language python

# Filter by time period
python github_trending.py --since weekly

# Combined filters
python github_trending.py --language javascript --since monthly
```

## Output Example

```
================================================================================
  GitHub Trending Repositories (25 found)
================================================================================

  1. owner/repo-name
     ⭐ 1234 stars | 🍴 56 forks | 📈 234 stars today
     📝 A cool project description
     🔤 Python
     🔗 https://github.com/owner/repo-name
```

## Requirements

- Python 3.6+
- `requests`
- `beautifulsoup4`

Install dependencies:

```bash
pip install requests beautifulsoup4
```