# Weather Forecast Scraper

Fetches and displays 3-day weather forecast for any city using wttr.in.

## Features

- Fetches current weather conditions
- Displays 3-day forecast with temperature, humidity, rain chance
- Clean formatted output with emoji indicators
- No API key required (uses wttr.in)

## Usage

```bash
# Default city (London)
python weather_forecast.py

# Specify city
python weather_forecast.py --city "New York"

# Indian cities
python weather_forecast.py --city Mumbai
python weather_forecast.py --city Delhi
python weather_forecast.py --city Bangalore
```

## Output Example

```
============================================================
  Weather Forecast for London
============================================================

  🌡️  Current Conditions:
     Temperature: 15°C (feels like 14°C)
     Condition:   Partly cloudy
     Humidity:    72%
     Wind:        12 km/h
     Pressure:    1015 mb
     Visibility:  10 km

  📅  3-Day Forecast:
  Date         Max    Min    Avg  Rain% Humidity Condition
  ------------ ------ ------ ------ ------ -------- ---------------
  2026-10-11    17°C    11°C    14°C    10%      70% Partly cloudy
  2026-10-12    16°C    10°C    13°C    40%      75% Light rain
  2026-10-13    15°C     9°C    12°C    60%      80% Moderate rain
```

## Requirements

- Python 3.6+
- `requests`

Install dependencies:

```bash
pip install requests
```