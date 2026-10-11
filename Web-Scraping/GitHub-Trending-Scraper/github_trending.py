"""
GitHub Trending Scraper
Scrapes GitHub trending repositories and displays them in a clean format.

Usage:
    python github_trending.py [--language LANGUAGE] [--since SINCE]

Requirements:
    pip install requests beautifulsoup4
"""

import argparse
import sys
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://github.com/trending"


def build_url(language=None, since=None):
    """Build the GitHub trending URL with optional filters."""
    url = BASE_URL
    if language:
        url += f"/{language}"
    if since:
        url += f"?since={since}"
    return url


def parse_repos(soup):
    """Extract trending repositories from the parsed HTML."""
    repos = []
    articles = soup.find_all("article", class_="Box-row")

    for article in articles:
        repo_data = {}

        # Repo name and link
        repo_link = article.find("h2").find("a")
        if repo_link:
            repo_data["name"] = repo_link.get_text(strip=True).replace("\n", "").replace(" ", "")
            repo_data["url"] = urljoin("https://github.com", repo_link["href"])

        # Description
        desc = article.find("p", class_="col-9")
        repo_data["description"] = desc.get_text(strip=True) if desc else "No description"

        # Language
        lang = article.find("span", itemprop="programmingLanguage")
        repo_data["language"] = lang.get_text(strip=True) if lang else "N/A"

        # Stars and forks
        star_count = article.find("a", href=lambda x: x and "stargazers" in x)
        repo_data["stars"] = star_count.get_text(strip=True) if star_count else "0"

        fork_count = article.find("a", href=lambda x: x and "forks" in x)
        repo_data["forks"] = fork_count.get_text(strip=True) if fork_count else "0"

        # Today's stars
        today_stars = article.find("span", class_="d-inline-block float-sm-right")
        repo_data["stars_today"] = today_stars.get_text(strip=True) if today_stars else "N/A"

        repos.append(repo_data)

    return repos


def display_repos(repos):
    """Display repos in a formatted way."""
    if not repos:
        print("No trending repositories found.")
        return

    print(f"\n{'='*80}")
    print(f"  GitHub Trending Repositories ({len(repos)} found)")
    print(f"{'='*80}\n")

    for i, repo in enumerate(repos, 1):
        print(f"  {i}. {repo['name']}")
        print(f"     ⭐ {repo['stars']} stars | 🍴 {repo['forks']} forks | 📈 {repo['stars_today']} today")
        print(f"     📝 {repo['description']}")
        print(f"     🔤 {repo['language']}")
        print(f"     🔗 {repo['url']}")
        print()


def scrape_trending(language=None, since=None):
    """Main function to scrape and display trending repos."""
    url = build_url(language, since)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    print(f"Fetching: {url}")
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    repos = parse_repos(soup)
    display_repos(repos)

    return repos


def main():
    parser = argparse.ArgumentParser(
        description="Scrape GitHub trending repositories"
    )
    parser.add_argument(
        "--language",
        help="Filter by programming language (e.g., python, javascript)",
    )
    parser.add_argument(
        "--since",
        choices=["daily", "weekly", "monthly"],
        help="Time period for trending (default: daily)",
    )
    args = parser.parse_args()

    try:
        scrape_trending(language=args.language, since=args.since)
    except requests.RequestException as e:
        print(f"Error fetching data: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()