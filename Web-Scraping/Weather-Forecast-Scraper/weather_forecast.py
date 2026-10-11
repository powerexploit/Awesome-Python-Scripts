"""
Weather Forecast Scraper
Fetches and displays 3-day weather forecast for any city using wttr.in.

Usage:
    python weather_forecast.py [--city CITY] [--format FORMAT]

Requirements:
    pip install requests beautifulsoup4
"""

import argparse
import json
import sys

import requests

WTTR_URL = "https://wttr.in/{city}?format=j1"


def fetch_weather(city):
    """Fetch weather data from wttr.in API."""
    url = WTTR_URL.format(city=city)
    headers = {"User-Agent": "curl/7.68.0"}

    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
    return response.json()


def parse_current_condition(data):
    """Extract current weather conditions."""
    current = data.get("current_condition", [{}])[0]
    return {
        "temperature": current.get("temp_C", "N/A"),
        "feels_like": current.get("FeelsLikeC", "N/A"),
        "humidity": current.get("humidity", "N/A"),
        "description": current.get("weatherDesc", [{}])[0].get("value", "N/A"),
        "wind_speed": current.get("windspeedKmph", "N/A"),
        "pressure": current.get("pressure", "N/A"),
        "visibility": current.get("visibility", "N/A"),
    }


def parse_forecast(data):
    """Extract 3-day forecast."""
    forecasts = []
    weather = data.get("weather", [])

    for day in weather:
        date = day.get("date", "N/A")
        hourly = day.get("hourly", [])

        # Use midday data as representative
        midday = next((h for h in hourly if h.get("time") == "1200"), hourly[0] if hourly else {})

        forecasts.append({
            "date": date,
            "max_temp": day.get("maxtempC", "N/A"),
            "min_temp": day.get("mintempC", "N/A"),
            "avg_temp": day.get("avgtempC", "N/A"),
            "description": midday.get("weatherDesc", [{}])[0].get("value", "N/A"),
            "chance_of_rain": midday.get("chanceofrain", "N/A"),
            "humidity": midday.get("humidity", "N/A"),
            "wind_speed": midday.get("windspeedKmph", "N/A"),
        })

    return forecasts


def display_weather(city, current, forecasts):
    """Display weather in a formatted way."""
    print(f"\n{'='*60}")
    print(f"  Weather Forecast for {city.title()}")
    print(f"{'='*60}\n")

    print("  🌡️  Current Conditions:")
    print(f"     Temperature: {current['temperature']}°C (feels like {current['feels_like']}°C)")
    print(f"     Condition:   {current['description']}")
    print(f"     Humidity:    {current['humidity']}%")
    print(f"     Wind:        {current['wind_speed']} km/h")
    print(f"     Pressure:    {current['pressure']} mb")
    print(f"     Visibility:  {current['visibility']} km")
    print()

    print("  📅  3-Day Forecast:")
    print(f"  {'Date':<12} {'Max':>6} {'Min':>6} {'Avg':>6} {'Rain%':>6} {'Humidity':>8} {'Condition'}")
    print(f"  {'-'*12} {'-'*6} {'-'*6} {'-'*6} {'-'*6} {'-'*8} {'-'*15}")

    for fc in forecasts:
        print(
            f"  {fc['date']:<12} {fc['max_temp']:>5}°C {fc['min_temp']:>5}°C {fc['avg_temp']:>5}°C "
            f"{fc['chance_of_rain']:>5}% {fc['humidity']:>7}% {fc['description']}"
        )

    print()


def main():
    parser = argparse.ArgumentParser(
        description="Fetch and display weather forecast for any city"
    )
    parser.add_argument(
        "--city",
        default="London",
        help="City name for weather forecast (default: London)",
    )
    args = parser.parse_args()

    try:
        data = fetch_weather(args.city)
        current = parse_current_condition(data)
        forecasts = parse_forecast(data)
        display_weather(args.city, current, forecasts)
    except requests.RequestException as e:
        print(f"Error fetching weather for '{args.city}': {e}", file=sys.stderr)
        sys.exit(1)
    except (KeyError, IndexError) as e:
        print(f"Error parsing weather data: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()